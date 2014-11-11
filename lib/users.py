import falcon
import simplejson as json

class UsersResource:
    def on_get( self, req, resp ):
        resp.body = json.dumps({'message': 'Hello world!'})
        resp.status = falcon.HTTP_200
