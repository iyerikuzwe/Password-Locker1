
class User:
    """
    Class that generates new instances of users.
    """

    list_of_users = []

    def __init__(self, user_name,gender, password):
        self.user_name = user_name
        self.gender = gender
        self.password = password

    def save_user(self):
        '''
        function that saves User objects into list_of_users
        '''
        self.list_of_users.append(self)



