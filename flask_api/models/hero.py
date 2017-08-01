from base_model import BaseModel
from peewee import *

class Hero(BaseModel):
    name = CharField()
