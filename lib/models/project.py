import peewee as pw

from user import User
from property import Property
from line_item import LineItem

class ProjectStatus(BaseModel):
    id = pw.PrimaryKeyField()
    status = pw.CharField()

class Project(BaseModel):
    shortname = pw.CharField( index=True )
    description = pw.CharField()
    project_status_id = pw.ForeignKeyField(ProjectStatus, related_name="projects", index=True)
    created_at = pw.CharField()
    updated_at = pw.CharField()

class UserProject(BaseModel):
    id = pw.PrimaryKeyField()
    user_id = pw.ForeignKeyField(User, related_name="projects", index=True)
    property_id = pw.ForeignKeyField(Property, related_name="projects")
    project_id = pw.ForeignKeyField(Project, related_name="owners")

class ProjectImage(BaseModel):
    image_uuid = pw.UUIDField( primary_key=True )
    project_id = pw.ForeignKeyField( Project, related_name="images", index=True )
    li_id = pw.ForeignKeyField( LineItem, related_name="images", index=True )
    created_at = pw.DateTimeField( default=datetime.datetime.now )

class ProjectNote(BaseModel):
    id = pw.PrimaryKeyField()
    note = pw.CharField()
    created_at = pw.DateTimeField( default=datetime.datetime.now )

