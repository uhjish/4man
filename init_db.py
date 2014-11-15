import peewee as pw
from playhouse.db_url import connect
from lib.models.user import *
from lib.models.contractor import *
from lib.models.line_item import *
from lib.models.property import *
from lib.models.project import *


db = connect("postgres://localhost:5432/4man")

db.create_tables([Skill,Contractor,Phase,Area,Category,LineItem,LineSubitem,LineSubitemCost,LineContractor,LineContractorNote,ProjectStatus,Project,UserProject,Channel,SiteImage,ProjectNote,Property,PropertyContact,PropertyNote,User,UserNotes,Role,UserRole,Contact,ContactChannel,UserContact], safe=True)

