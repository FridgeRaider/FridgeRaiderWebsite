import re
from copy import deepcopy
from datetime import datetime, timedelta
from json import JSONEncoder, loads
from random import randint
import re

from urllib import urlencode
from uuid import uuid4

import gridfs

from mogo import Model, Field, ReferenceField, ASC, DESC
from mogo.model import ObjectId
from mogo.connection import Connection as mogo_connection
from operator import itemgetter
from pymongo import DESCENDING,ASCENDING
from pymongo.errors import OperationFailure

from stemming.porter import stem
from settings import torn_settings as settings
from tornado.escape import xhtml_escape



now = datetime.now
_mentions_re = re.compile(r'(?<!\S)@((?![\d:]+(?:[pa]m)?\b)\w+)', re.I)


class ModelEncoder(JSONEncoder):
    """
    A generic Model encoder that will hopefully get the results of a
    model's _d() dictionary as input.
    """
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, ReferenceField):
            return [str(type(obj)), obj.value_type, obj.mro]
        return JSONEncoder.default(self, obj)


class FRModel(Model):
    """
    Base class for all Frideraider models that defines _d() so that models
    can be serialized, say to a JSON format. There is a recursionlimit
    parameter to limit the number of Reference
    """
    def _d(self, recursionlimit=2):
        """
        Build a dict from all non-callable entities attached to our object.
        """
        d = dict()
        for (k,v) in self.__dict__.iteritems():
            if not callable(v):
                prop = getattr(type(self),k,None)
                if prop:
                    if isinstance(prop, ReferenceField):
                        v2 = getattr(self, k)
                        for f in [v, v2]:
                            if isinstance(f, GPModel):
                                # limit depth of references we serialize
                                if recursionlimit > 0:
                                    recursionlimit -= 1
                                    d[k] = f._d(recursionlimit)
                                else:
                                    d[k] = (f._id)
                    else:
                        # otherwise, just put the value ...
                        t=(bool,basestring,int,long,float,list,dict,tuple,set)
                        if isinstance(v,t):
                            d[k] = v
        return d

    def _json(self, recursionlimit=10):
        " Returns a json representation of the dict from _d() "
        return ModelEncoder().encode(self._d(recursionlimit))


class User(FRModel):
    """
    Our definition of a system user.
    """
    displayName = Field()
    email = Field()
    password = Field()
    dateJoined = Field(datetime,default=now)
    lastLogin = Field(datetime,default=now)
    ingredients = Field(list,default=[])


class Ingredient(FRModel):
    """
    This is a model of what ingredients might look like
    """
    displayName = Field()

    #This will be EnumField(("Stuff","Stuff1","Stuff2")) once
    #we figure shit out
    category = Field()
    dateEntered = Field(datetime,default=now)
    quantity = Field(float,default=1)
    quantityUnit = Field(default=None)
    UPC = Field(default=None)
    expirationDate = Field(datetime,default=now)

