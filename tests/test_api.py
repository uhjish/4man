import requests as rq
from requests import Request, Session
import json

def jpp( jobj ):
    return json.dumps( jobj , sort_keys=True, indent=4, separators=(',', ': ')) 

class JWTRequestor:
    def __init__(self, sess=None, base_uri="", auth_endpoint ="", credentials={}):
        if not sess:
            self.session = Session()
        else:
            self.session = sess
        self.base_uri = base_uri
        self.get_auth_token( auth_endpoint, credentials)
    def get_auth_token( self, endpoint, credentials={} ):
        # send a post request to the auth handler
        auth_uri = self.base_uri + endpoint
        r = rq.post( auth_uri, data=json.dumps(credentials))
        print  jpp( r.json() )
        token = r.json()['token'].encode('ascii')
        self.token = "Bearer %s" % token
    def req( self, endpoint, typ="GET", data={} ):
        r = Request(typ, self.base_uri + endpoint, data=json.dumps(data))
        prepped = s.prepare_request(r)
        prepped.headers["Authorization"]= self.token
        prepped.headers["content-type"]='application/json'
        return s.send( prepped )

#-- setup
cred = {'username':'test','password':'test'}
s = Session()
#-- authenticate
jr = JWTRequestor(s, "http://127.0.0.1:8000", "/api/v1/auth", cred)

get_res = jr.req('/api/user')
print jpp(get_res.json())

#-- make post request

post_res = jr.req('/api/contact', typ='POST',
        data = {'fullname':'yertle turtle',
                'street':'sesame st.',
                'city':'somewhere',
                'state':'ON',
                'zipcode':12345})
print jpp( post_res.json() )

put_res = jr.req('/api/contact/2', typ='PUT',
        data = {'fullname':'Mcyertle Mcturtle',
                'street':'sensamilla st.',
                'city':'somewhere',
                'state':'NO',
                'zipcode':54321})
print jpp( put_res.json() )

del_res = jr.req('/api/contact/2', typ='DELETE')
print  del_res.json() 

#-- make get request
get_res = jr.req('/api/contact')
print jpp(get_res.json())
