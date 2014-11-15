import peewee as pw
from base import BaseModel
from user import User

class Skill(BaseModel):
    id = pw.PrimaryKeyField()
    name = pw.CharField()
    description = pw.CharField()

class Contractor(BaseModel):
    user = pw.ForeignKeyField(User, related_name="contracting", primary_key=True)
    skill = pw.ForeignKeyField(Skill, related_name="workers", index=True)
    rating = pw.IntegerField()
    description = pw.TextField()


