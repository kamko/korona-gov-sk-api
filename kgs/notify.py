import itertools
import logging

import requests
import telegram


def _format_msg(observation):
    return f'News from *korona.gov.sk*:\n' \
           f'- *Tested:* {observation.tested}\n' \
           f'- *Negative:* {observation.negative}\n' \
           f'- *Positive:* {observation.positive}\n' \
           f'- *Sync time (UTC):* {observation.sync_time}\n' \
           f'View history at: korona.kamko.dev/stats/all'


class NotificationPipeline:
    _notifier_providers = [
        lambda conf, formatter: TelegramNotifier.make_notifiers(conf, formatter),
        lambda conf, formatter: SlackNotifier.make_notifier(conf, formatter)
    ]

    def __init__(self, conf):
        self.pipeline = list(itertools.chain.from_iterable(
            (i(conf, _format_msg) for i in NotificationPipeline._notifier_providers)))

    def send_all(self, observation):
        for i in self.pipeline:
            try:
                i.send(observation)
            except Exception:
                logging.error(f'failed to send notification to {i}')


class TelegramNotifier:

    def __init__(self, token, chat_id, msg_provider):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id
        self.msg_provider = msg_provider

    def send_status(self, observation):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=self.msg_provider(observation),
            parse_mode="markdown"
        )

    @staticmethod
    def make_notifiers(conf, msg_provider):
        if conf.TELEGRAM_TARGETS is None:
            return []

        items = conf.TELEGRAM_TARGETS.rstrip(';').split(';')

        return [TelegramNotifier(j[0], j[1], msg_provider)
                for j in (i.split('~') for i in items)]


class SlackNotifier:
    def __init__(self, webhook_id, msg_provider):
        self.webhook_id = webhook_id
        self.msg_provider = msg_provider

    def send_status(self, observation):
        requests.post(
            url=f'https://hooks.slack.com/services/{self.webhook_id}',
            json={
                'text': self.msg_provider(observation)
            }
        )

    @staticmethod
    def make_notifier(conf, msg_provider):
        if conf.SLACK_TARGETS is None:
            return []

        return [SlackNotifier(i, msg_provider)
                for i in conf.SLACK_TARGETS.rstrip(';').split(';')]
