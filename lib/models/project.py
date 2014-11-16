import datetime
from __init__ import db
from user import User
from property import Property
from note import Note

notes_projects = db.table('notes_projects',
        db.Column( 'project_id', db.Integer, db.ForeignKey('project.id')),
        db.Column( 'note_id', db.Integer, db.ForeignKey('note.id')))


class ProjectStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())

class Project(db.Model):
    shortname = pw.CharField( index=True )
    description = db.Column(db.String())
    user = db.Column( db.Integer, db.ForeignKeyField('user.id') )
    property = db.Column( db.Integer, db.ForeignKeyField('property.id') )
    status = db.Column( db.Integer, db.ForeignKeyField('projectstatus.id') )
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())
    notes = db.relationship( 'Note', secondary=notes_projects, lazy='dynamic' ) 


