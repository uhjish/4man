import falcon
import lib.routes.things as things
import lib.routes.users as users


api = application = falcon.API()

things = things.ThingsResource()
users = users.UsersResource()

api.add_route('/things', things)
api.add_route('/user', users)



