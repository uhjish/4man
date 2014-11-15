from flask import Flask
#from flask.ext.admin import Admin
#from flask.ext.admin.contrib.peewee import ModelView
import peewee as pw
from playhouse.db_url import connect
from flask_peewee.rest import RestAPI, UserAuthentication
#from flask.ext.security import *
#from flask.ext.security import Security, PeeweeUserDatastore, \
#    UserMixin, RoleMixin, login_required
from lib.models.user import *
from flask_peewee.admin import Admin

db = connect("postgres://localhost:5432/4man")

app = Flask(__name__)
'''
# Setup Flask-Security
user_datastore = PeeweeUserDatastore(db, User, Role, UserRole)
security = Security(app, user_datastore)
user_datastore.create_role(name="admin", description="admin")
user_datastore.create_user(username="Ben", fullname="Ben Button", email='hello', password='password')
user_datastore.add_role_to_user('hello', "admin")
'''
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'



# Setup Flask-Security
#user_datastore = PeeweeUserDatastore(db, User, Role, UserRole)
#security = Security(app, user_datastore)

# Create a user to test with
#@app.before_first_request
def create_user():
    user_datastore.create_role(name="admin", description="admin")
    user_datastore.create_user(email='a@b.com', password='password', fullname='ben dover', username='bend')
    user_datastore.add_role_to_user('a@b.com', "admin")

api = RestAPI(app)
admin = Admin(app, auth)

# register our models so they are exposed via /api/<model>/
api.register(User)
api.register(Contact)
api.register(UserContact)

# Add administrative views here
admin.add_view(ModelView(User))
admin.add_view(ModelView(Contact))
admin.add_view(ModelView(UserContact))

api.setup()

app.run()
