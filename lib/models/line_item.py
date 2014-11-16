import datetime
from __init__ import db
from project import Project
from user import User

class Phase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())

li_contractor = db.Table('lineitem_contractor',
		db.Column('li_id', db.Integer(), db.ForeignKey('line_item.id')),
		db.Column('contractor_id', db.Integer(), db.ForeignKey('contractor.id')),
        db.Column('updated_at', db.DateTime,  default=datetime.datetime.now) )

class LineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.Integer, db.ForeignKey('project.id')) 
    phase = db.Column(db.Integer, db.ForeignKey('phase.id')) 
    area = db.Column(db.Integer, db.ForeignKey('area.id')) 
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String())
    description = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    updated_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True)
    linesubitems = db.relationship('LineSubitem', backref='parentitem', lazy='dynamic')
    contractors = db.relationship('Contractor', secondary=li_contractor, backref='lineitems', lazy='dynamic') 

class LineSubitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineitem =  db.Column(db.Integer, db.ForeignKey('line_item.id'))
    title = db.Column(db.String())
    description = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    updated_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True) 
    subitemcosts = db.relationship('LineSubitemCost', backref='parentsubitem', lazy='dynamic')

class LineSubitemCost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linesubitem =  db.Column(db.Integer, db.ForeignKey('line_subitem.id'))
    is_estimate = db.Column(db.Boolean)
    material_cost = db.Column( db.Numeric )
    labor_cost = db.Column( db.Numeric )
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True)
    
class SiteImage(db.Model):
    image_uuid = db.Column( db.String(), primary_key=True ) 
    project = db.Column( db.Integer, db.ForeignKey('project.id'))
    li = db.Column( db.Integer, db.ForeignKey('line_item.id'), nullable=True)
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )
