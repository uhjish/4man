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
    def __repr__(self):
        return self.status 

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column( db.Integer, db.ForeignKey('user.id') )
    property_id = db.Column( db.Integer, db.ForeignKey('property.id') )
    shortname = db.Column(db.String())
    desc= db.Column(db.String())
    status_id = db.Column( db.Integer, db.ForeignKey('project_status.id') )
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())
    notes = db.relationship( 'Note', secondary=notes_projects, lazy='joined' )
    line_items = db.relationship( 'LineItem', backref='parent_project', lazy='joined', join_depth=1)
    status = db.relationship( ProjectStatus )
    def __repr__(self):
        return self.shortname

