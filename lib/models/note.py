from __init__ import db
import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String())
    user_visible = db.Column(db.Boolean, default=False)
    contractor_visible = db.Column(db.Boolean, default=False)
    estimator_visible = db.Column(db.Boolean, default=False)
    created_at = db.Column( db.DateTime, default=datetime.datetime.now )

