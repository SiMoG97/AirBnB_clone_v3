#!/usr/bin/python3
"""connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route('/status', methods=["GET"], strict_slashes=False)
def status():
    """hbnb Status"""
    return jsonify(status="OK")
