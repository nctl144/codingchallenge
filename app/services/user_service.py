from app.models.user import User
from app.dao.user_dao import UserDao


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def insert_users(self, data):
        users = [User(user_data) for user_data in data]
        self.user_dao.insert_users(users)

    def retrieve_user_with_id(self, id):
        return self.user_dao.retrieve_user_with_id(id)

    def search_users(self, filters):
        self.validate_user_filters(filters)
        searched_users = self.user_dao.search_users(filters)

        self.user_dao.update_searched_user_count(searched_users)
        return searched_users

    def validate_user_filters(self, filters):
        for filter in filters:
            if filter not in User.FILTER_ATTRS:
                raise Exception("filter is not valid")
