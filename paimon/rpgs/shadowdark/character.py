import json
import random

from rpgs.shadowdark.settings import *

alignments = ['L','C','N']

charclass_data = json.loads(open(f'{PATH}/json/charclass.json').read())
titles_data = json.loads(open(f'{PATH}/json/titles.json').read())
backgrounds_data = json.loads(open(f'{PATH}/json/backgrounds.json').read())

class Character:
    # STR, DEX, CON, INT, WIS, CHA
    stats = []
    background: str = ''
    ancestry: str = ''
    charclass: str = ''
    alignment: str = ''
    title: str = ''
    languages: list[str] = ['common']
    diety: str = ''
    gear = {}
    gear_slots: int = 0
    name: str = ''
    level: int = 1
    xp: int = 0
    hp: list[int, int] = [0,0]

def randchar():
    char = Character()

    # 1) stats
    for i in range(6):
        char.stats.append(
            random.randint(3, 18)
        )

    # 1.5) background
    r = random.randint(0, 19)
    char.background = backgrounds_data[r]
    
    # 2) ancestory + 6) languages
    r = random.randint(1, 12)
    match r:
        case 1 | 2 | 3 | 4:
            char.ancestry = 'human'
            # ONE RANDOM LANGUAGE
        case 5 | 6:
            char.ancestry = 'elf'
            char.languages.append('elvish')
        case 7 | 8:
            char.ancestry = 'dwarf'
            char.languages.append('dwarvish')
        case 9 | 10:
            char.ancestry = 'halfling'
            # ONLY COMMON
        case 11:
            char.ancestry = 'half_orc'
            char.languages.append('orcish')
        case 12:
            char.ancestry = 'goblin'
            char.languages.append('goblin')
        case _:
            print(f'ERROR: Did not roll a correct value! Rolled: {r}')

    # 3) charclass
    r = random.randint(0, 3)
    charclasses = list(charclass_data)
    char.charclass = charclasses[r]

    # 4) alignment
    r = random.randint(0, 2)
    char.alignment = alignments[r]

    # 5) title
    r = random.randint(0, 4)
    # randomly pick a title based on class and alignment
    char.title = titles_data[char.charclass][char.alignment][r]

    # 7) diety
    # randomly choose a diety

    # 8) gear
    # randomly select gear using the table at the back

    # 9) randomly choose a name from a random names list

    # update the database with this character

    '''
    print('--CHARACTER--')
    print(f'Stats: {char.stats}')
    print(f'Background: {char.background}')
    print(f'Ancestry: {char.ancestry}')
    print(f'Class: {char.charclass}')
    print(f'Alignment: {char.alignment}')
    print(f'Title: {char.title}')
    '''
