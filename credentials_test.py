import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Fb", "12@34")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.acc_name,"Fb")
        self.assertEqual(self.new_credentials.acc_password, "12@34")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the list_of_creds
        '''
        self.new_credentials.save_credentials()  # saving the new credentials
        self.assertEqual(len(Credentials.list_of_creds), 1)

    def test_save_several_credentials(self):
        '''
        test_save_several_credentials method adds new multiple credentials to list_of_creds
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Pinterest", "56@78")  # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.list_of_creds), 2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.list_of_creds = []

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our list of credentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Pinterest", "56@78")  # new credential
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()  # Deleting a credentials object
            self.assertEqual(len(Credentials.list_of_creds), 1)

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a credentials by nameand display information for user
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Pinterest", "56@78")  # new credential
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("Pinterest")

        self.assertEqual(found_credentials.acc_name, test_credentials.acc_name)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.list_of_creds)


if __name__ == '__main__':
    unittest.main()
