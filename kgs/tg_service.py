import logging

import telegram

from kgs import AppConfiguration

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

bot = telegram.Bot(token=AppConfiguration.TELEGRAM_TOKEN)


def send_status(observation):
    bot.send_message(
        chat_id=AppConfiguration.TELEGRAM_CHAT_ID,
        text=f'News from *korona.gov.sk*:\n'
             f'- *Tested:* {observation.tested}\n'
             f'- *Negative:* {observation.negative}\n'
             f'- *Positive:* {observation.positive}\n'
             f'- *Sync time (UTC):* {observation.sync_time}\n'
             f'-- provided by korona.kamko.dev --',
        parse_mode="markdown"
    )
