import unicodedata
import utils 
from passlib.hash import sha256_crypt
from tornapp.models import User,Ingredient
from pymongo import *
from datetime import datetime, timedelta

def main():
    db = utils.connect_db('FridgeRaider',True)
    collection = db['user']
    ingredientOne = Ingredient(
                                    displayName = "Flour",
                                    category = "Baking",
                                    quantity = 5.0,
                                    quantityUnit = 'ib.',
                                    expirationDate = datetime.now()+timedelta(days=14)
                               )

    print ingredientOne.displayName
    print collection.find_one()
    userOne = User(
                    displayName = "Jordan",
                    email = "jordan@tamu.edu",
                    password = sha256_crypt.encrypt('password'),
                    ingredients = [ingredientOne]
    )
    
    collection.insert(userOne)

if __name__=="__main__":
    main()
