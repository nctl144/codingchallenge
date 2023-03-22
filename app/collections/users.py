from challenge.models.user import User

class Users:
    def __init__(self, data=[]):
        self.users = {}
        for user_data in data:
            self.usersUser(user_data)
    

    
