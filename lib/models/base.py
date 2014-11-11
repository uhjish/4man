import peewee as pw

#initialize db from config here
db = None

class BaseModel(pw.Model):
    class Meta:
        database = db
