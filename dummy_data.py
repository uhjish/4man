from lib.models import db
from lib.models.user import *
from lib.models.contractor import *
from lib.models.line_item import *
from lib.models.project import *
from lib.models.property import *
from lib.models.note import *

def init_models():
    db.session.add( Role(name='client', desc='estimate system client') )
    db.session.add( Role(name='user', desc='estimate system user') )
    db.session.add( Role(name='admin', desc='estimate system admin') )
    db.session.commit()

    db.session.add( Channel(name='phone', desc='telephone number'))
    db.session.add( Channel(name='mobile', desc='mobile number'))
    db.session.add( Channel(name='email', desc='email address'))
    db.session.add( Channel(name='other', desc='other contact id'))
    db.session.commit()

    db.session.add( Phase(name='demolition', desc='demolition phase'))
    db.session.add( Phase(name='construction', desc='construction phase'))
    db.session.add( Phase(name='cleanup', desc='cleanup phase'))
    db.session.commit()

    db.session.add( Area(name='bathroom', desc='bathroom area'))
    db.session.add( Area(name='living', desc='living area'))
    db.session.add( Area(name='kitchen', desc='kitchen area'))
    db.session.add( Area(name='bedroom', desc='bedroom area'))
    db.session.add( Area(name='garage', desc='garage area'))
    db.session.add( Area(name='deck', desc='deck area'))
    db.session.commit()

    db.session.add( Category(name='painting', desc='painting work'))
    db.session.add( Category(name='plumbing', desc='plumbing work'))
    db.session.add( Category(name='masonry', desc='masonry work'))
    db.session.add( Category(name='electrical', desc='electrical work'))
    db.session.commit()

    db.session.add( Skill(name='painting', desc='painting work'))
    db.session.add( Skill(name='plumbing', desc='plumbing work'))
    db.session.add( Skill(name='masonry', desc='masonry work'))
    db.session.add( Skill(name='electrical', desc='electrical work'))
    db.session.commit()

    db.session.add( ProjectStatus(status='initiated'))
    db.session.add( ProjectStatus(status='sitevisit'))
    db.session.add( ProjectStatus(status='estimation'))
    db.session.add( ProjectStatus(status='contract'))
    db.session.add( ProjectStatus(status='construction'))
    db.session.add( ProjectStatus(status='billing'))
    db.session.add( ProjectStatus(status='completed'))
    db.session.commit()

#--- Now the actual dummy project

    con1 = Contact(fullname='Jeremiah Worthington', street='123 Dickens Ave', city='Monte Carlo', state='MD', zipcode=54321)
    con2 = Contact(fullname='Theodore Finchbottom', street='444 Underhill Ct', city='San Sebastian', state='MD', zipcode=55555)
    con3 = Contact(fullname='Isadore Thistlethorpe', street='555 Hemingway Dr', city='Mazatlan', state='MD',zipcode=44444)
    ch1 = ContactItem(channel_id=1, identifier='410-555-5555', desc='home phone number', label='home phone',contact=con1)
    ch2 = ContactItem(channel_id=1, identifier='410-777-7777', desc='office phone number', label='office phone', contact=con3)
    ch3 = ContactItem(channel_id=2, identifier='410-444-7777', desc='mobile phone number', label='mobile phone', contact=con1)
    prop = Property(name='bartleby',desc='1920s tudor on a cul-de-sac', street='123 Dickens Ave', city='Monte Carlo', state='MD', zipcode=54321)
    prop2 = Property(name='winsor',desc='a-frame on a quiet side street', street='321 Huckleberry Terr', city='Del Monaco', state='MD', zipcode=12345)
    db.session.add(con1)
    db.session.add(con2)
    db.session.add(con3)
    db.session.add(ch1)
    db.session.add(ch2)
    db.session.add(ch3)
    db.session.add(prop)
    db.session.add(prop2)
    db.session.commit()

    pr = Project( shortname='Test Project', desc='test angular functionality')

    db.session.add(pr)

    li1 = LineItem(title='remove existing tile', desc='removal of existing tile with explanation')
    li2 = LineItem(title='cleanup tile debris', desc='a rambunctious racoon ran into the road roaring')
    li3 = LineItem(title='install new tile', desc='the road really rattled the roaring racoon')

    db.session.add(li1)
    db.session.add(li2)
    db.session.add(li3)

    db.session.commit()

