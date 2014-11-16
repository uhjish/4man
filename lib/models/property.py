import datetime
from __init__ import db
from user import User
from user import Contact

note_property = db.Table('note_property',
        db.Column('property_id', db.Integer, db.ForeignKey('property.id')),
        db.Column('note_id', db.Integer, db.ForeignKey('note.id')))

contact_property = db.Table('contact_property',
        db.Column('property_id', db.Integer, db.ForeignKey('property.id')),
        db.Column('contact_id', db.Integer, db.ForeignKey('contact.id')))

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column( db.Integer, db.ForeignKey('user.id') )
    name = db.Column(db.String())
    description = db.Column(db.String())
    street =  db.Column(db.String())
    city =  db.Column(db.String())
    state =  db.Column(db.String())
    zipcode = db.Column(db.Integer)
    latitude = db.Column( db.Numeric )
    longitude = db.Column( db.Numeric )
    notes = db.relationship( 'Note', secondary='note_property', lazy='joined')
    contacts = db.relationship( 'Contact', secondary='contact_property', lazy='joined')

