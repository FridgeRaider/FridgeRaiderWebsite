# This file will test that the authentication of a user logging in is done
# correctly. This will include logging in through the website and the mobile
# application. This test file will also ensure that getting or setting the
# current user is done correctly.

import unittest
import json
import loginhandler

from mock import Mock, patch

class TestRegistration(unittest.TestCase):
    # This test will test whether the get function will render the registration page.
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
    # or may not return a successful registration. This simply tests that the post goes
    # through with valid data.
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

    # This test will test whether the post operation works for invalid data. This data
    # should return a page that explains the errors. This simply tests that the post goes
    # through with invalid data and returns an error message.
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

    # This test will test whether the post operation works for successful registration 
    # data. This data is expected to validate correctly and return evidence of a
    # successful registration. 
    def test_post_successfulRegistration(self, mock_mongo_query)
        self.assert(false)

    # This test will test whether the post operation works for an unsuccessful 
    # registration data. This data is expected to fail validation and return evidence of
    # an unsuccessful registration. 
    def test_post_unsuccessfulRegistration(self, mock_mongo_query)
        self.assert(false)

if __name__ == '__main__':
    unittest.main()
