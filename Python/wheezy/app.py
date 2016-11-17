from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
import json


class WelcomeHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        quote = {
            'message': 'Hello, World!'
        }
        response.write(json.dumps(quote))
        return response

all_urls = [
    url('', WelcomeHandler, name='default')
]

options = {}
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options=options
)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    try:
        make_server('', 8888, main).serve_forever()
    except KeyboardInterrupt:
        pass