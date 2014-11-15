import peewee as pw
from playhouse.db_url import connect
import datetime
#initialize db from config here

db = connect("postgres://localhost:5432/4man")

class BaseModel(pw.Model):
    def __repr__( self ):
        ctyp = type(self).__name__
        lbl = None
        try:
            lbl = str(self.id)
        except:
            lbl = 'unk' 
        return '%s:%s' % (ctyp, lbl)
    class Meta:
        database = db
