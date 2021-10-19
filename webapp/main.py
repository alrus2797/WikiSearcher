from typing_extensions import IntVar
import bottle
from bottle import redirect, request, response, route, static_file, view

import app_init
from firebase_admin import db

import json

pages_ref = db.reference('/pages')
ranks_ref = db.reference('/ranks')
idx_ref = db.reference('/indexes')


def enable_cors(fn):
    def wrapper(*args, **kwargs):
        bottle.response.set_header("Access-Control-Allow-Origin", "*")
        bottle.response.set_header(
            "Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        bottle.response.set_header(
            "Access-Control-Allow-Headers", "Origin, Content-Type")

        # skip the function if it is not needed
        if bottle.request.method == 'OPTIONS':
            return

        return fn(*args, **kwargs)
    return wrapper


@route('/')
@enable_cors
def index():
    return 'WikiSearcher'


@route('/search')
def search():
    word = request.query['query']
    print(word)
    if not word:
        return redirect('/')

    page_ids = idx_ref.child(word).get()
    print("Page ids fetched", len(page_ids))
    results = {}
    for pid in page_ids:
        print("Fetching: ", pid)
        page_url = pages_ref.child(pid).get()
        results[page_url] = page_ids[pid]

    return json.dumps(results)


@route('/src/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./src')


bottle.run(reloader=True, debug=True)
