from peewee import *
from playhouse.sqlite_ext import *

from paimon import settings

db = SqliteDatabase(f'{settings.DB_CONNECTION}/shadowdark.db')

class Characters(Model):
    # basics
    name = CharField()
    ancestry = CharField()
    charclass = CharField()
    title = CharField()
    alignment = CharField()
    background = CharField()

    # stats
    level = IntegerField()
    xp = IntegerField()
    hp = IntegerField()
    max_hp = IntegerField()

    # JSONs
    stats = JSONField()
    talents = JSONField()
    spells = JSONField()
    coins = JSONField()
    gear = JSONField()

    # gear slots
    gear_slots = IntegerField()

    class Meta:
        database = db

# connect to the database
db.connect()
db.create_tables([
    Characters,
])
db.close()
