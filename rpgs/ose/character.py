import random
import json

import diceroll

class Character:
    # STR INT WIS DEX CON CHA
    stats = [0, 0, 0, 0, 0, 0]
    char_class: str
    saving_throws = []
    hit_dice: str
    max_hp: int
    current_hp: int
    alignment: str
    level = 1
    xp = 0
    languages = ['common']

def get_stat_modifier(stat: int):
    if stat == 3:
        return -3
    elif stat > 3 and stat <= 5:
        return -2
    elif stat > 5 and stat <= 8:
        return -1
    elif stat > 8 and stat <= 12:
        return 0
    elif stat > 12 and stat <= 15:
        return 1
    elif stat > 15 and stat <= 17:
        return 2
    elif stat == 18:
        return 3
    else:
        return None

def randchar():
    json_file = open('./rpgs/ose/char_class.json')
    j_char_class = json.loads(json_file.read())

    char = Character()

    alignments = ['lawful', 'neutral', 'chaotic']
    classes = list(j_char_class)

    # 1) randomly generate stats
    for i in range(6):
        char.stats[i] = diceroll.roll('3d6')

    # 2) randomly pick a class
    char.char_class = classes[random.randint(0, 3)]

    # 6) note saving throws
    char.saving_throws = j_char_class[char.char_class]['saving_throws']

    # 7) roll hit points
    char.max_hp = diceroll.roll(j_char_class[char.char_class]['hit_dice'][1:])
    char.current_hp = char.max_hp

    # 8) choose alignment
    char.alignment = alignments[random.randint(0, 2)]

    # 9) note known languages
    char.languages.append(char.alignment)
    intelligence_mod = get_stat_modifier(char.stats[1])
    if intelligence_mod > 0:
        # we have multiple languages to note
        extra_langs = intelligence_mod

    # 10) buy equipment
    # 11) note armor class
    # 12) note level and XP     - DONE
    # 13) name character
