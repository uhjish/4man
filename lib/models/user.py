from __init__ import db
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from note import Note

import datetime

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

notes_users = db.Table('notes_users',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('note_id', db.Integer, db.ForeignKey('note.id')))

contacts_users = db.Table('contacts_users',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('contact_id', db.Integer, db.ForeignKey('contact.id')))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='joined'))
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)
    notes = db.relationship('Note', secondary=notes_users, lazy='joined')
    contact = db.relationship('Contact')
    projects = db.relationship('Project', backref='client', lazy='joined')
    def __repr__(self):
        return 'User[email=%s]' % self.email

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc= db.Column(db.String(255))
    def __repr__(self):
        return self.name 




class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String())
    street = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zipcode = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now )
    items = db.relationship('ContactItem', lazy='joined')
    def __repr__(self):
        return "%s - %s" % (self.fullname , self.city )

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    def __repr__(self):
        return self.name 

class ContactItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String())
    channel_id = db.Column( db.Integer, db.ForeignKey('channel.id') ) 
    contact_id = db.Column( db.Integer, db.ForeignKey('contact.id') )
    desc= db.Column( db.String() )
    label = db.Column(db.String())
    is_primary = db.Column(db.Boolean, default=False)
    channel = db.relationship( Channel )
    contact = db.relationship( Contact )
    def __repr__(self):
        return "%d,%d:%s" %(self.contact_id, self.id, self.label) 
