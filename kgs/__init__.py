# import atexit

# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from kgs.config import AppConfiguration, StaticConfiguration
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
    pass


def schedule_job(app):
    pass
#     scheduler = BackgroundScheduler()
#     # scheduler.add_job(func=lambda:..., trigger="interval",
#     #                   seconds=...)
#     print("scheduler - start")
#     scheduler.start()
#
#     atexit.register(lambda: scheduler.shutdown())
