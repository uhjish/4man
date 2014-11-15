import peewee as pw
import datetime

from base import BaseModel
from project import Project
from user import User


class Phase(BaseModel):
    id = pw.PrimaryKeyField()
    phase = pw.CharField()

class Area(BaseModel):
    id = pw.PrimaryKeyField()
    area = pw.CharField()

class Category(BaseModel):
    id = pw.PrimaryKeyField()
    category = pw.CharField()

class LineItem(BaseModel):
    id = pw.PrimaryKeyField()
    project = pw.ForeignKeyField(Project, related_name="line_items", index=True)
    phase = pw.ForeignKeyField(Phase, index=True)
    area = pw.ForeignKeyField(Area, index=True)
    category = pw.ForeignKeyField(Category, index=True)
    title = pw.CharField()
    description = pw.TextField()
    is_active = pw.BooleanField(default=True)
    updated_at = pw.DateTimeField( default=datetime.datetime.now )
    deleted_at = pw.DateTimeField()

class LineSubitem(BaseModel):
    id = pw.PrimaryKeyField()
    li = pw.ForeignKeyField(LineItem, related_name="subitems", index=True)
    title = pw.CharField()
    description = pw.CharField()
    is_active = pw.BooleanField(default=True)
    updated_at = pw.DateTimeField( default=datetime.datetime.now )
    deleted_at = pw.DateTimeField() 

class LineSubitemCost(BaseModel):
    id = pw.PrimaryKeyField()
    subitem = pw.ForeignKeyField(LineSubitem, related_name="costs", index=True)
    is_estimate = pw.BooleanField()
    material_cost = pw.DoubleField()
    labor_cost = pw.DoubleField()
    created_at = pw.DateTimeField( default=datetime.datetime.now )
    deleted_at = pw.DateTimeField()

class LineContractor(BaseModel):
    id = pw.PrimaryKeyField()
    li = pw.ForeignKeyField(LineItem, related_name="contractors", index=True)
    user = pw.ForeignKeyField(User, related_name="li_awarded", index=True)
    updated_at = pw.DateTimeField( default=datetime.datetime.now )

class LineContractorNote(BaseModel):
    id = pw.PrimaryKeyField()
    li_contractor = pw.ForeignKeyField(LineContractor, related_name="notes", index=True)
    note = pw.CharField()
    updated_at = pw.DateTimeField( default=datetime.datetime.now )
    
class SiteImage(BaseModel):
    image_uuid = pw.UUIDField( primary_key=True )
    project = pw.ForeignKeyField( Project, related_name="images", index=True )
    li = pw.ForeignKeyField( LineItem, related_name="images", index=True )
    created_at = pw.DateTimeField( default=datetime.datetime.now )
