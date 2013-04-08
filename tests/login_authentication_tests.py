#This file will test that the authentication of a user logging in is done correctly. This will include logging in through the website and the mobile application.
import unittest
from tornapp.views.account import LoginHandler

class TestLogin(unittest.TestCase):

    def testget(self):
        loginHandler = LoginHandler()
        renderedPage = loginHandler.get()

    def testpost(self):
        loginHandler = LoginHandler()
        
