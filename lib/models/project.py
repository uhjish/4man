import peewee as pw
import datetime

from base import BaseModel
from user import User
from property import Property

class ProjectStatus(BaseModel):
    id = pw.PrimaryKeyField()
    status = pw.CharField()

class Project(BaseModel):
    shortname = pw.CharField( index=True )
    description = pw.CharField()
    project_status = pw.ForeignKeyField(ProjectStatus, related_name="projects", index=True)
    created_at = pw.CharField()
    updated_at = pw.CharField()

class UserProject(BaseModel):
    id = pw.PrimaryKeyField()
    user = pw.ForeignKeyField(User, related_name="projects", index=True)
    property = pw.ForeignKeyField(Property, related_name="projects")
    project = pw.ForeignKeyField(Project, related_name="owners")


class ProjectNote(BaseModel):
    id = pw.PrimaryKeyField()
    note = pw.CharField()
    created_at = pw.DateTimeField( default=datetime.datetime.now )

