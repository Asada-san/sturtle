# from api.App.models import Counter
# from api.App import db
from flask import url_for, render_template, request, Blueprint, redirect, \
    send_from_directory
from flask import make_response, jsonify, send_file
from flask_cors import CORS
import os
# import requests
# from bs4 import BeautifulSoup
import json
import time
import random
import pprint

api = Blueprint('api', __name__)
CORS(api, resources={r"/api/*": {"origins": "*"}}, support_credentials=True)


@api.route("/calc", methods=['POST'])
def calc():
    # user_input = request.get_json()

    results = {'A': 1,
               'B': 2,
               'C': 3,
               'D': 4,
               'E': 5}

    res = make_response(jsonify(results), 200)

    return res

# @api.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)
#
#
# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(api.root_path, endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)
