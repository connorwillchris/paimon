from peewee import *

import settings

db = SqliteDatabase(f'{settings.DB_CONNECTION}')

class Users(Model):
    discord_id = BigIntegerField()
    guild_id = BigIntegerField()
    class Meta:
        database = db

db.connect()
db.create_tables([
    Users
])
