import falcon
import json
 
class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'message': 'Hello, World!'
        }

        resp.body = json.dumps(quote)
 
api = falcon.API()
api.add_route('/', QuoteResource())