from flask import Flask, render_template, request, url_for, redirect
from flask.ext.security import SQLAlchemyUserDatastore, Security, \
		login_required, current_user, logout_user
from flask.ext.security.utils import encrypt_password, verify_password
from flask.ext.restless import APIManager, ProcessingException
from flask.ext.login import user_logged_in
from flask.ext.admin import Admin
from flask_jwt import JWT, jwt_required
from lib.models import db
from lib.models.user import *
from admin import AdminModelView, UserModelView, LogoutView, LoginView
import os
# Configuration  ==============================================================
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# Setup Flask-Security  =======================================================
security = Security(app, user_datastore)

# JWT Token authentication  ===================================================
jwt = JWT(app)
@jwt.authentication_handler
def authenticate(username, password):
	user = user_datastore.find_user(email=username)
	if username == user.email and verify_password(password, user.password):
		return user
	return None

@jwt.user_handler
def load_user(payload):
	user = user_datastore.find_user(id=payload['user_id'])
	return user

# Views  ======================================================================
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/mypage')
@login_required
def mypage():
	return render_template('mypage.html')

@app.route('/logout')
def log_out():
	logout_user()
	return redirect(request.args.get('next') or '/')

# Flask-Restless API  =========================================================
@jwt_required()
def auth_func(**kw):
	return True

apimanager = APIManager(app, flask_sqlalchemy_db=db)
apimanager.create_api(Contact,
	methods=['GET', 'POST', 'DELETE', 'PUT'],
	url_prefix='/api/v1',
	collection_name='free_stuff',
	include_columns=['data1', 'data2', 'user_id'])
apimanager.create_api(Contact,
	methods=['GET', 'POST', 'DELETE', 'PUT'],
	url_prefix='/api/v1',
	preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
	collection_name='protected_stuff',
	include_columns=['data1', 'data2', 'user_id'])

# Flask-Admin  ================================================================
admin = Admin(app)
admin.add_view(UserModelView(User, db.session, category='Auth'))
admin.add_view(AdminModelView(Role, db.session, category='Auth'))
admin.add_view(AdminModelView(Contact, db.session))
admin.add_view(LogoutView(name='Logout', endpoint='logout'))
admin.add_view(LoginView(name='Login', endpoint='login'))

# Bootstrap  ==================================================================
def init_app():
	db.init_app(app)
	db.create_all()

def create_test_models():
	user_datastore.create_user(email='test', password=encrypt_password('test'))
	user_datastore.create_user(email='test2', password=encrypt_password('test2'))
	stuff = Contact(street='abc',city='def',state='NB',zipcode=12345)
	db.session.add(stuff)
	stuff = Contact(street='2 abc',city='dddef',state='XB',zipcode=12345)
	db.session.add(stuff)
	db.session.commit()

@app.before_first_request
def bootstrap_app():
	if not app.config['TESTING']:
		if db.session.query(User).count() == 0:
			create_test_models();
port = int(os.environ.get('PORT', 5000))
# Start server  ===============================================================
if __name__ == '__main__':		
	with app.app_context():
		init_app()
	app.run( debug=True, port=port)
