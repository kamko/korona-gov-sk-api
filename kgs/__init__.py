import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from kgs import kgov_service
from kgs.config import AppConfiguration, StaticConfiguration
from kgs.db import db
from kgs.ma import ma
from kgs.root import blueprint as root_blueprint


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
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: kgov_service.load_latest_data(app), trigger="interval",
                      seconds=AppConfiguration.CHECK_FREQUENCY)
    print("scheduler - started")
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
