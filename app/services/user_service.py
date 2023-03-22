from app.models.user import User
from app.dao.user_dao import UserDao


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def insert_users(self, data):
        for user_data in data:
            user = User(user_data)

            self.user_dao.insert_user(user)

    def retrieve_user_with_id(self, id):
        return self.user_dao.retrieve_user_with_id(id)
