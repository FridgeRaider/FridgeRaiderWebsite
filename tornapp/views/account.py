import re
import tornado.web
from tornado.escape import json_encode, json_decode
from viewlib import route, BaseHandler, async_yield
import utils
from passlib.hash import sha256_crypt
from operator import itemgetter

from ..models import User,Ingredient




@route("/account/login")
class LoginHandler(BaseHandler):

  def get(self):
    self.render("account/login.html", next=self.get_argument("next","/"), message=self.get_argument("error","") )

  def post(self):
    email = self.get_argument("email", "")
    password = self.get_argument("password", "")
    db = utils.connect_db('FridgeRaider')
            
    u = User.search(email=email.lower()).first()
    if sha256_crypt.verify(password,u.password):
        self.set_current_user(u)
        self.redirect("/account/home")

    else:
        error_msg = tornado.escape.url_escape("Invalid Login")
        self.redirect("/account/login?error="+error_msg)


              
    

@route("/account/register")
class RegisterHandler(LoginHandler):

  def get(self):
    error = self.get_argument("error", "")    
    self.render(  "account/register.html", next=self.get_argument("next","/"), error=error)

  def post(self):
    args = self.request.arguments
    print args
    db = utils.connect_db('FridgeRaider')
    collection = db['User']
    u = User.search(email=args['email'][0].lower()).first()
    if u:
        error_msg = u"?error=" + tornado.escape.url_escape("Email already registered")
        self.redirect(u"/account/register" + error_msg)
        
    elif args['password1'][0] != args['password2'][0]:
        error_msg = u"?error=" + tornado.escape.url_escape("Passwords did not match")
        self.redirect(u"/account/register" + error_msg)
    else:
        user = User(
                    displayName = args['Name'][0],
                    email = args['email'][0],
                    password = sha256_crypt.encrypt(args['password1'][0]),
                    ingredients = []
                   )

        user.save()
        self.set_current_user(user)

        self.redirect("/account/home")

@route("/account/home")
class AccountHome(BaseHandler):

  def get(self):
    self.render("account/home.html")
    

@route("/account/logout")
class Logout(BaseHandler):
    def get(self):
        self.clear_current_user()
        self.redirect("/")


