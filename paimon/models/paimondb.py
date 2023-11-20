from peewee import *

import settings

db = SqliteDatabase(f'{settings.DB_CONNECTION}/paimon.db')

# users table
class Users(Model):
    discord_id      = BigIntegerField()
    guild_id        = BigIntegerField()

    # the amount of campaigns and characters this user owns
    campaigns       = IntegerField(default=0)
    characters      = IntegerField(default=0)

    class Meta:
        database = db

class Campaigns(Model):
    name            = CharField()
    description     = TextField()

    # foreign keys
    user_id         = ForeignKeyField(Users, backref='id')
    guild_id        = ForeignKeyField(Users, backref='guild_id')
    # all the players in the campaign - Users, not characters
    player_0        = ForeignKeyField(Users, backref='id')
    player_1        = ForeignKeyField(Users, backref='id')
    player_2        = ForeignKeyField(Users, backref='id')
    player_3        = ForeignKeyField(Users, backref='id')
    player_4        = ForeignKeyField(Users, backref='id')
    player_5        = ForeignKeyField(Users, backref='id')
    player_6        = ForeignKeyField(Users, backref='id')
    player_7        = ForeignKeyField(Users, backref='id')

    class Meta:
        database = db

class Rpgs(Model):
    name = CharField()
    long_name = TextField()

    class Meta:
        database = db

# connect to the database
db.connect()

# create the tables in the database

db.create_tables([
    Users, Campaigns, Rpgs,
])

# we're done with the database, close now
db.close()
