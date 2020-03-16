from flask import Blueprint, jsonify, redirect, url_for

import kgs.kgov_service as kgov_service
from kgs.ma import ObservationSchema

blueprint = Blueprint('root', __name__)

_obs_schema = ObservationSchema()


@blueprint.route('/stats')
def stats():
    return _obs_schema.jsonify(kgov_service.get_latest())


@blueprint.route('/stats/all')
def stats_all():
    return _obs_schema.jsonify(kgov_service.get_all(), many=True)


@blueprint.route('/')
def redirect_root():
    return _obs_schema.redirect(url_for('.stats'), code=301)
