#!/usr/bin/python3
""" index"""

from flask import jsonify
from . import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
