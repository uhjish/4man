import falcon
import lib.things as things
import lib.users as users
api = application = falcon.API()

things = things.ThingsResource()
users = users.UsersResource()

api.add_route('/things', things)
api.add_route('/user', users)



