from __init__ import db
from user import User, Contact

contractor_skills = db.Table('contractor_skills',
        db.Column('contractor_id',db.Integer, db.ForeignKey('contractor.id')),
        db.Column('skill_id',db.Integer, db.ForeignKey('skill.id')),
        db.Column('rating', db.Integer),
        db.Column('details', db.String()))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

class Contractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contact = db.Column( db.Integer, db.ForeignKey( 'contact.id' ) )
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    skills = db.relationship( 'Skill', secondary='contractor_skills', 
                            backref=db.backref('contractors', lazy='dynamic'))
    description = db.Column(db.String())


