import datetime
from __init__ import db
from project import Project
from user import User

class Phase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    def __repr__(self):
        return self.name

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
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
    area = db.relationship('Area', lazy='joined')
    phase = db.relationship('Phase', lazy='joined')
    category = db.relationship('Category', lazy='joined')
    linesubitems = db.relationship('LineSubitem', backref='parentitem', lazy='joined')
    contractors = db.relationship('Contractor', secondary=li_contractor, backref='lineitems', lazy='joined') 
    images = db.relationship('SiteImage', backref='parentitem', lazy='joined')
    def __repr__(self):
        return self.title

class LineSubitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineitem_id =  db.Column(db.Integer, db.ForeignKey('line_item.id'))
    desc= db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    est_material = db.Column( db.Numeric )
    est_labor = db.Column( db.Numeric )
    act_material = db.Column( db.Numeric )
    act_labor = db.Column( db.Numeric )
    updated_at = db.Column( db.DateTime, default=datetime.datetime.now )
    deleted_at = db.Column( db.DateTime, nullable=True) 
    def __repr__(self):
        return self.desc

class SiteImage(db.Model):
    image_uuid = db.Column( db.String(), primary_key=True ) 
    #image_ext = db.Column( db.String(4) );
    project_id = db.Column( db.Integer, db.ForeignKey('project.id'))
    lineitem_id = db.Column( db.Integer, db.ForeignKey('line_item.id'), nullable=True)
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )
    def __repr__(self):
        return 'image: %d' % self.image_uuid
