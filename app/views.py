from app import app
from flask import session, request, make_response

@app.route('/')
def main_page():
    response = make_response(u'Boom!')
    response.cache_control.max_age = 40
    return response
