from flask_restful import Resource,reqparse
from models.user import UserModel

class UserResgister(Resource):
    parsing = reqparse.RequestParser()
    parsing.add_argument('username',
                         type=str,
                         required=True,
                         help="This field cannot be left blank"

                         )
    parsing.add_argument('password',
                         type=int,
                         required=True,
                         help="This field cannot be left blank"

                         )

    def post(self):
        data = UserResgister.parsing.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':'user with this username already exist'}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {'Message': 'user name created successfully'}, 201
