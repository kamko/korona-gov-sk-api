from flask import Blueprint, redirect, url_for

import kgs.korona_service as korona_service
from kgs.ma import ObservationSchema

blueprint = Blueprint('root', __name__)

_obs_schema = ObservationSchema()


@blueprint.route('/stats')
def stats():
    return _obs_schema.jsonify(korona_service.get_latest())


@blueprint.route('/stats/all')
def stats_all():
    return _obs_schema.jsonify(korona_service.get_all(), many=True)


@blueprint.route('/')
def redirect_root():
    return redirect(url_for('.stats'), code=301)
