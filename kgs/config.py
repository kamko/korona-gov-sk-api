from flask_env import MetaFlaskEnv


class StaticConfiguration():
    APP_NAME = 'kamko/korona-gov-sk-api'
    VERSION = '0.0.1'
    USER_AGENT = f'{APP_NAME}:{VERSION}'

    KORONA_GOV_SK_URL = 'https://www.korona.gov.sk/'


class AppConfiguration(metaclass=MetaFlaskEnv):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = r'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CHECK_FREQUENCY = 5

    TELEGRAM_TARGETS = None  # "<token>~<chat-id>;<token>~<chat-id>;"
    SLACK_TARGETS = None  # "<webhookid>;<webhookid>;"
