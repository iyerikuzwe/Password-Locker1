import unittest #unittest module imported
from user import User #Importing class User from module user

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("firstUser", "Female", "23@45")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_user.user_name, "firstUser")
          self.assertEqual(self.new_user.gender, "Female")
          self.assertEqual(self.new_user.password, "23@45")

if __name__ == '__main__':
    unittest.main()
