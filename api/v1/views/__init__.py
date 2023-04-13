#!/usr/bin/python3
"""
    create Blueprint that make application work in smaller parts
"""


from flask import Blueprint


app_views = Blueprint('/api/v1', __name__)
from api.v1.views.index import *
