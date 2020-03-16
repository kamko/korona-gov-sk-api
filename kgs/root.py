from flask import Blueprint, jsonify, redirect, url_for

import kgs.kgov_service as kgov_service

blueprint = Blueprint('root', __name__)


@blueprint.route('/stats')
def stats():
    return jsonify(kgov_service.get_stats())


@blueprint.route('/')
def redirect_root():
    return redirect(url_for('.stats'), code=301)
