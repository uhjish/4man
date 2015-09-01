from flask import Flask
from flask.ext.restful import Resource, reqparse

class UsersAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, 
                required=True, help='username missing', location = 'json')
        self.reqparse.add_argument('first', type=str, 
                required=True, help='firstname missing', location = 'json')
        self.reqparse.add_argument('middle', type=str, location = 'json')
        self.reqparse.add_argument('last', type=str, 
                required=True, help='lastname missing', location = 'json')
        self.reqparse.add_argument('details', type=str, location = 'json')
    def get( self, id )
        pass

def email( in_str ):
    if validate_email( in_str ):
        return True
    else:
        raise ValidationError("%s is not a valid email" % in_str)


class UserLoginAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email_id", type=email, required=True, location='json')
        self.reqparse.add_argument("password", type=str, required=True, location='json')
    
