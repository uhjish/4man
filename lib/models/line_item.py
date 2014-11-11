import peewee as pw

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
    project_id = pw.ForeignKeyField(Project, related_name="line_items", index=True)
    phase_id = pw.ForeignKeyField(Phase, index=True)
    area_id = pw.ForeignKeyField(Area, index=True)
    category_id = pw.ForeignKeyField(Category, index=True)
    title = pw.CharField()
    description = pw.TextField()

class LineItemImage(BaseModel):
    li_id = pw.ForeignKeyField(LineItem, index=True)
    image_uuid = pw.UUIDField()
    created_at = pw.DateTimeField(default=datetime.datetime.now)
