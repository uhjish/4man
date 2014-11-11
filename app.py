import falcon
import lib.models.things as things
import lib.models.users as users
api = application = falcon.API()

things = things.ThingsResource()
users = users.UsersResource()

api.add_route('/things', things)
api.add_route('/user', users)



