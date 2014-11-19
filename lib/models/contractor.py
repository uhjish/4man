from __init__ import db
from user import User, Contact
from sqlalchemy.ext.associationproxy import association_proxy

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    def __repr__(self):
        return self.name 

class Contractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contact_id = db.Column( db.Integer, db.ForeignKey( 'contact.id' ) )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    desc= db.Column(db.String())
    user = db.relationship( User, backref='contractor_role')
    contact = db.relationship( Contact )
    def __repr__(self):
        return self.name 
class ContractorSkill(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    contractor_id = db.Column(db.Integer, db.ForeignKey('contractor.id'))
    skill_id = db.Column( db.Integer, db.ForeignKey('skill.id'))
    rating = db.Column( db.Integer)
    details = db.Column( db.String())
    contractor = db.relationship( Contractor, backref='skillset' )
    skill = db.relationship( Skill, backref='skillset')

Contractor.skills = association_proxy("contractor_skill", "skill")
