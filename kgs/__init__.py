import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from kgs.config import AppConfiguration, StaticConfiguration
from kgs.db import db
from kgs.korona_service import KoronaService
from kgs.ma import ma
from kgs.root import blueprint as root_blueprint

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def create_app():
    app = Flask(StaticConfiguration.APP_NAME)
    app.config.from_object(AppConfiguration)
    app.config.from_object(StaticConfiguration)

    register_plugins(app)
    register_blueprints(app)

    schedule_job(app)

    return app


def register_blueprints(app):
    app.register_blueprint(root_blueprint, url_prefix='/')


def register_plugins(app):
    db.init_app(app)
    db.create_all(app=app)

    ma.init_app(app)


def schedule_job(app):
    from kgs.notify import NotificationPipeline
    from kgs.client import KGSClient, VKClient

    scheduler = BackgroundScheduler()

    client_map = {
        'korona.gov.sk': KGSClient,
        'virus-korona.sk': VKClient
    }

    client = client_map[AppConfiguration.DATA_SOURCE]()
    service = KoronaService(app, client)

    notification_pipeline = NotificationPipeline(AppConfiguration)
    scheduler.add_job(func=lambda: service.load_latest_data(app, notification_pipeline),
                      trigger="interval",
                      seconds=AppConfiguration.CHECK_FREQUENCY)
    print("scheduler - started")
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
