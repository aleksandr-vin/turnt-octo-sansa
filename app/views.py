from app import app
from flask import session, request, make_response

@app.route('/')
def main_page():
    etag = '123qwe321sss'

    response = make_response(u'Boomzzzzzzzzzzzzzzzzxx!')
    response.headers['ETag'] = etag
    response.headers['Last-Modified'] = 'Mon, 29 Jun 2015 01:02:03 GMT'

    response.cache_control.no_cache = True
#    response.cache_control.no_store = True
    response.cache_control.max_age = 100
    response.cache_control.no_transform = True
    response.cache_control.must_revalidate = True
#    response.cache_control.private = True
#    response.cache_control.proxy_revalidate = True
    response.cache_control.public = True
#    response.cache_control.s_maxage = 100

    if request.headers.get('If-None-Match') == etag:
        return response, 304

    return response
