import datetime
from __init__ import db
from user import User
from property import Property
from note import Note

notes_projects = db.Table('notes_projects',
        db.Column( 'project_id', db.Integer, db.ForeignKey('project.id')),
        db.Column( 'note_id', db.Integer, db.ForeignKey('note.id')))


class ProjectStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String())
    description = db.Column(db.String())
    user = db.Column( db.Integer, db.ForeignKey('user.id') )
    property = db.Column( db.Integer, db.ForeignKey('property.id') )
    status = db.Column( db.Integer, db.ForeignKey('project_status.id') )
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())
    notes = db.relationship( 'Note', secondary=notes_projects, lazy='dynamic' ) 


