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
        self.new_user = User("firstUser", "Male", "12@34")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_user.user_name, "firstUser")
          self.assertEqual(self.new_user.gender, "Male")
          self.assertEqual(self.new_user.password, "12@34")

if __name__ == '__main__':
    unittest.main()
