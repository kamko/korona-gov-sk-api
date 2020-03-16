import logging

from kgs.client import KGSClient
from kgs.db import Observation, db
from kgs.tg_service import send_status

client = KGSClient()


def _latest_query():
    return Observation.query \
        .order_by(Observation.sync_time.desc())


def _save_observation(obs):
    db.session.add(obs)
    db.session.commit()


def _should_save(old, new):
    if old is None:
        return True

    return old.negative != new.negative \
           or old.positive != new.positive \
           or old.tested != new.tested


def load_latest_data(app):
    with app.app_context():
        logging.info('fetching latest data')
        stats = client.load_stats()

        current = Observation(**stats)
        last_known = _latest_query().first()

        if _should_save(last_known, current):
            logging.info(f'new data found! {current}')
            _save_observation(current)
            send_status(current)


def get_latest():
    return _latest_query().first_or_404()


def get_all():
    return Observation.query \
        .order_by(Observation.sync_time.desc()) \
        .all()
