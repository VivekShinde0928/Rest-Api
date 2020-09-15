from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)  # get is another way to acces dictionary key to gives value
    if user is not None and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']  # payload takes all the conent of JWT token & sets to variable user_id
    return UserModel.find_by_id(user_id)
