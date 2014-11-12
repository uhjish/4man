import peewee as pw

from base import *
from user import User
from user import Contact

class Property(BaseModel):
    id = pw.PrimaryKeyField()
    user_id = pw.ForeignKeyField( User, related_name="properties", index=True )
    name = pw.CharField()
    description = pw.CharField()
    street = pw.CharField( index=True )
    city = pw.CharField( index=True )
    state = pw.CharField( index=True )
    zipcode = pw.IntegerField( index=True )
    latitude = pw.DoubleField()
    longitude = pw.DoubleField()

class PropertyContact(BaseModel):
    id = pw.PrimaryKeyField()
    property_id = pw.ForeignKeyField( Property, related_name="contacts", index=True )
    contact_id = pw.ForeignKeyField( Contact, related_name="assoc_props", index=True )

class PropertyNote(BaseModel):
    id = pw.PrimaryKeyField()
    property_id = pw.ForeignKeyField( Property, related_name="notes", index=True )
    note = pw.CharField()
    created_at = pw.DateTimeField( default=datetime.datetime.now )
