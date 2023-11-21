import random

from models.characters import Characters
from models.users import Users

def randomchar(ctx):
    character = Characters()
    
    # basics
    name = ''
    charclass = ''
    level = 1
    xp = 0
    alignment = ''
    # stats
    stats = [0,0,0,0,0,0]
    # hp and combat
    hp_max = 0
    hp = hp_max
    ac = 0
    # wealth
    gp, pp, cp, sp, ep = 0

