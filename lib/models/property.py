import datetime
from __init__ import db
from user import User
from user import Contact

note_property = db.Table('note_property',
        db.Column('property_id', db.Integer, db.ForeignKey('property.id')),
        db.Column('note_id', db.Integer, db.ForeignKey('note.id')))
'''
contact_property = db.Table('contact_property',
        db.Column('property_id', db.Integer, db.ForeignKey('property.id')),
        db.Column('contact_id', db.Integer, db.ForeignKey('contact.id')))
'''


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contact_id = db.Column( db.Integer, db.ForeignKey( 'contact.id' ) )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship( User, backref='client_role')
    contact = db.relationship( Contact )
    def __repr__(self):
        return self.name 


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column( db.Integer, db.ForeignKey('user.id') )
    name = db.Column(db.String())
    desc= db.Column(db.String())
    street =  db.Column(db.String())
    city =  db.Column(db.String())
    state =  db.Column(db.String())
    zipcode = db.Column(db.Integer)
    latitude = db.Column( db.Numeric )
    longitude = db.Column( db.Numeric )
    notes = db.relationship( 'Note', secondary='note_property', lazy='joined')
    # contacts = db.relationship( 'Contact', secondary='contact_property', lazy='joined')
    projects = db.relationship( 'Project', backref='property', lazy='joined')
    def __repr__(self):
        return self.name
