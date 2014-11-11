import peewee as pw

#db = Postgres
#TODO: setup db config tool

class User(BaseModel):
    id = pw.PrimaryKeyField()
    username = pw.CharField(index=True, unique=True)
    first = pw.CharField(index=True)
    middle = pw.CharField()
    last = pw.CharField(index=True)
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    is_active = pw.BooleanField()

class UserLogin(BaseModel):
    user_id = pw.ForeignKeyField( User, 
                                  related_name="login", 
                                  primary_key=True )
    email_id = pw.CharField()
    password = pw.CharField()
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    last_login = pw.DateTimeField(default=None)
    is_enabled = pw.BooleanField(default=True)

class Role(BaseModel):
    id = pw.PrimaryKeyField()
    role = pw.CharField()

class UserRole(BaseModel):
    user_id = pw.ForeignKeyField(User, related_name="roles")
    role_id = pw.ForeignKeyField(Role, related_name="users")
    class Meta:
        primary_key = CompositeKey('user_id','role_id')

class Contact(BaseModel):
    id = pw.PrimaryKeyField()
    first = pw.CharField()
    middle = pw.CharField()
    last = pw.CharField()
    street = pw.CharField()
    city = pw.CharField()
    state = pw.CharField()
    zipcode = pw.CharField()

class ContactChannel(BaseModel):
    id = pw.PrimaryKeyField()
    contact_id = pw.ForeignKeyField(Contact, related_name="channels", index=True)
    contact_type = pw.ForeignKeyField(Channel, related_name="contacts_using", index=True)
    contact_info = pw.CharField(index=True)


