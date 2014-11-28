from datetime import timedelta
import os

pgurl = os.environ.get('HEROKU_POSTGRESQL_SILVER_URL')

class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = ''

	APP_NAME = 'ApplicationName'
	SECRET_KEY = 'add_secret'
	JWT_EXPIRATION_DELTA = timedelta(days=30)
	JWT_AUTH_URL_RULE = '/api/v1/auth'
	SECURITY_REGISTERABLE = True
	SECURITY_RECOVERABLE = True
	SECURITY_TRACKABLE = True
	SECURITY_PASSWORD_HASH = 'sha512_crypt'
	SECURITY_PASSWORD_SALT = 'add_salt'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/4man'

class DevelopmentConfig(Config):
	#SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/4man'
        SQLALCHEMY_DATABASE_URI = 'postgresql://dvyjrgvbtlqzqq:X-beURc-TZPoKNEs4nYZcGwROM@ec2-54-83-5-151.compute-1.amazonaws.com:5432/d51l61lh2nmpl0'
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
	DEBUG = True
        IMAGE_BUCKET = '4man-static-storage'

class HerokuConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://dvyjrgvbtlqzqq:X-beURc-TZPoKNEs4nYZcGwROM@ec2-54-83-5-151.compute-1.amazonaws.com:5432/d51l61lh2nmpl0'
    DEBUG = True

class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite://'
	TESTING = True
