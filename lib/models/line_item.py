import datetime
from __init__ import db
from project import Project
from user import User

class Phase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    line_items = db.relationship('LineItem',backref='phase',lazy='dynamic')
    def __repr__(self):
        return self.name

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    line_items = db.relationship('LineItem',backref='area',lazy='dynamic')
    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    line_items = db.relationship('LineItem',backref='category',lazy='dynamic')
    def __repr__(self):
        return self.name

li_contractor = db.Table('lineitem_contractor',
		db.Column('li_id', db.Integer(), db.ForeignKey('line_item.id')),
		db.Column('contractor_id', db.Integer(), db.ForeignKey('contractor.id')),
        db.Column('updated_at', db.DateTime,  default=datetime.datetime.now) )

class LineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id')) 
    phase_id = db.Column(db.Integer, db.ForeignKey('phase.id')) 
    area_id = db.Column(db.Integer, db.ForeignKey('area.id')) 
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String())
    desc= db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    updated_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True)
    linesubitems = db.relationship('LineSubitem', backref='parentitem', lazy='joined')
    contractors = db.relationship('Contractor', secondary=li_contractor, backref='lineitems', lazy='joined') 
    images = db.relationship('SiteImage', backref='parentitem', lazy='joined')
    def __repr__(self):
        return 'project: %d - %d' % (self.project_id, self.id )

class LineSubitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineitem_id =  db.Column(db.Integer, db.ForeignKey('line_item.id'))
    title = db.Column(db.String())
    desc= db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    updated_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True) 
    subitemcosts = db.relationship('LineSubitemCost', backref='parentsubitem', lazy='joined')
    def __repr__(self):
        return 'project: %d - %d.%d' % (self.parentitem.project_id, self.lineitem_id, self.id)

class LineSubitemCost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linesubitem_id =  db.Column(db.Integer, db.ForeignKey('line_subitem.id'))
    is_estimate = db.Column(db.Boolean)
    material_cost = db.Column( db.Numeric )
    labor_cost = db.Column( db.Numeric )
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True)
    def __repr__(self):
        return str(is_estimate) + " %s, %s" % (self.material_cost,self.labor_cost)
    
class SiteImage(db.Model):
    image_uuid = db.Column( db.String(), primary_key=True ) 
    project_id = db.Column( db.Integer, db.ForeignKey('project.id'))
    lineitem_id = db.Column( db.Integer, db.ForeignKey('line_item.id'), nullable=True)
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )
    def __repr__(self):
        return 'image: %d' % self.id
