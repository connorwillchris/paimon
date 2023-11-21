from peewee import *
from playhouse.sqlite_ext import *

import settings
import models.users as users

db = SqliteDatabase(settings.DB_CONNECTION)

# characters are based on OSR D&D
class Characters(Model):
    name = CharField()
    owner_id = ForeignKeyField(users.Users, backref='id')
    # basics
    charclass = CharField()
    level = IntegerField()
    xp = IntegerField()
    alignment = CharField()
    # stats
    strength = IntegerField()
    dexterity = IntegerField()
    constitution = IntegerField()
    intelligence = IntegerField()
    wisdom = IntegerField()
    charisma = IntegerField()
    # hit points and combat
    hp = IntegerField()
    hp_max = IntegerField()
    ac = IntegerField()
    # wealth
    gp = IntegerField()
    pp = IntegerField()
    ep = IntegerField()
    sp = IntegerField()
    cp = IntegerField()
    # other stuff
    spellcaster = BooleanField()
    spells = JSONField()
    equipment = JSONField()
    class Meta:
        database = db
