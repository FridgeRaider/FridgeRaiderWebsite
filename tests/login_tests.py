# This file will test that the authentication of a user logging in is done
# correctly. This will include logging in through the website and the mobile
# application. This test file will also ensure that getting or setting the
# current user is done correctly.

import unittest
import json
import loginhandler

from mock import Mock, patch

class TestLogin(unittest.TestCase):
    # This test will test whether the get function will render the login page.
    def test_get(self, mock_mongo_query):
        # Create a mock result for the requests.get call
        request = Mock()
        # set any other attributes on the request that you need
        mock_mongo_query.return_value = []

        application = Mock()
        handler = LoginHandler(application, request)
        handler.write = Mock()

        handler.get('')

        self.assertEqual(handler.write.call_args_list, json.dumps({'some': 'data'}))

    # This test will test whether the post operation works for valid data. This data may
    # or may not return a successful login. This simply tests that the post goes through
    # with valid data.
    def test_post_validData(self, mock_mongo_query)
        # Create a mock result for the requests.get call
        request = Mock()
        # set any other attributes on the request that you need
        mock_mongo_query.return_value = ["email": "test@gmail.com", "password": "password"]

        application = Mock()
        handler = LoginHandler(application, request)
        handler.write = Mock()

        handler.post('')

        self.assertEqual(handler.write.call_args_list, json.dumps({'some': 'data'}))

    # This test will test whether the post operation works for in valid data. This data
    # should return a page that explains the errors. This simply tests that the post goes
    # through with in valid data and returns an error message.
    def test_post_invalidData(self, mock_mongo_query)
        # Create a mock result for the requests.get call
        request = Mock()
        # set any other attributes on the request that you need
        mock_mongo_query.return_value = ["email": "", "password": "password"]

        application = Mock()
        handler = LoginHandler(application, request)
        handler.write = Mock()

        handler.post('')

        self.assertEqual(handler.write.call_args_list, json.dumps({'some': 'data'}))

    # This test will test whether the post operation works for successful login data. This
    # data is expected to validate correctly and return evidence of a successful login. 
    def test_post_successfulLogin(self, mock_mongo_query)
        self.assert(false)

    # This test will test whether the post operation works for an unsuccessful login
    # data. This data is expected to fail validation and return evidence of an
    # unsuccessful login. 
    def test_post_unsuccessfulLogin(self, mock_mongo_query)
        self.assert(false)

    # This test verifies that the getCurrentUser function returns the user that is currently
    # logged into the application. 
    def test_getCurrentUser(self, mock_mongo_query)
        self.assert(false)

    # This test verifies that the setCurrentUser function sets the current user to the
    # user given in the input. 
    def test_setCurrentUser(self, mock_mongo_query)
        self.assert(false)

    # This test verifies that the clearCurrentUser function clears the currently logged in
    # user. 
    def test_clearCurrentUser(self, mock_mongo_query)
        self.assert(false)

if __name__ == '__main__':
    unittest.main()
