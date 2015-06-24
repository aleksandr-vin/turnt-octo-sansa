from app import app
from flask import session, request, make_response

@app.route('/')
def main_page():
    response = make_response(u'Boom!')
    response.headers['Cache-Control'] = 'max-age=20'
    return response
