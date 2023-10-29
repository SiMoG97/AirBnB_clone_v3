#!/usr/bin/python3
"""connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnb Status"""
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    pass
