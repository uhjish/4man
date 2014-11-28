from hashlib import sha1
import datetime, os, json, base64, hmac, urllib
import uuid
TIME_FORMAT = "%Y-%m-%dT%H:%M:%sZ"
POLICY_TEMPLATE = '''
{
"expiration": "%s",
"conditions": [
        {"bucket": "%s"},
        ["starts-with", "$key", ""],
        ["content-length-range", 0, 10485760],
        ["starts-with","$Content-Type",""]
    ]
}
'''
class ImageS3:
    def __init__( self, bucket, access_key, secret_key ):
        self.bucket = bucket
        self.access_key = access_key
        self.secret_key = secret_key
    def getURL(self):
        return "https://%s.s3.amazon.com" % self.bucket
    def generate_token(self):
        exp = datetime.datetime.utcnow().strftime(TIME_FORMAT)
        policy = POLICY_TEMPLATE % (exp, self.bucket)
        policy = base64.b64encode( policy )
        print self.bucket, exp

        hsh = hmac.new( self.secret_key, policy, sha1 ).digest()
        hsh = base64.b64encode( hsh )
        
        return {    "file_id":      str(uuid.uuid4()),
                    "policy":       policy,
                    "signature":    hsh,
                    "key":          self.access_key }

