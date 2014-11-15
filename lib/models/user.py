import peewee as pw
from flask_peewee.auth import BaseUser
from flask.ext.security import UserMixin, RoleMixin
import datetime

from base import BaseModel
#db = Postgres
#TODO: setup db config tool

class Role(BaseModel, RoleMixin):
    name = pw.CharField(unique=True)
    description = pw.CharField(null=True)


class User(BaseModel, UserMixin):
    email = pw.CharField()
    username = pw.CharField()
    password = pw.CharField()
    fullname = pw.CharField(index=True)
    details = pw.CharField(default='')
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    confirmed_at = pw.DateTimeField(default=datetime.datetime.now)
    last_login = pw.DateTimeField(default=datetime.datetime.now)
    active = pw.BooleanField(default=True)

class UserRole(BaseModel):
    user = pw.ForeignKeyField(User, related_name="roles")
    role = pw.ForeignKeyField(Role, related_name="users")
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

class UserNotes(BaseModel):
    id = pw.PrimaryKeyField()
    user = pw.ForeignKeyField(User, related_name="notes", index=True)
    note = pw.CharField()
    user_visible = pw.BooleanField(default=False)
    contractor_visible = pw.BooleanField(default=False)
    estimator_visible = pw.BooleanField(default=True)
    created_at = pw.DateTimeField(default=datetime.datetime.now, index=True)

class Contact(BaseModel):
    id = pw.PrimaryKeyField()
    fullname = pw.CharField()
    street = pw.CharField()
    city = pw.CharField()
    state = pw.CharField()
    zipcode = pw.CharField()

class Channel(BaseModel):
    id = pw.PrimaryKeyField()
    name = pw.CharField()
    desc = pw.CharField()

class ContactChannel(BaseModel):
    id = pw.PrimaryKeyField()
    contact = pw.ForeignKeyField(Contact, related_name="channels", index=True)
    contact_type = pw.ForeignKeyField(Channel, related_name="contacts_using", index=True)
    contact_info = pw.CharField(index=True)

class UserContact(BaseModel):
    id = pw.PrimaryKeyField()
    user = pw.ForeignKeyField( User, related_name="contacts")
    contact = pw.ForeignKeyField( Contact, related_name="user")
    is_primary = pw.BooleanField()
    label = pw.CharField()


