import json
import random
import diceroll

from rpgs.shadowdark.settings import PATH

alignments = ['L','C','N']

class Character:
    # STR, DEX, CON, INT, WIS, CHA
    stats = []
    background: str = ''
    ancestry: str = ''
    charclass: str = ''
    alignment: str = ''
    title: str = ''
    languages: list[str] = []
    diety: str = ''
    gear = {}
    gear_slots: int = 0
    name: str = ''
    level: int = 1
    xp: int = 0
    hp: list[int, int] = [0,0]

def randchar():
    char = Character()

    charclass_data = json.loads(open(f'{PATH}/json/charclass.json').read())
    titles_data = json.loads(open(f'{PATH}/json/titles.json').read())
    backgrounds_data = json.loads(open(f'{PATH}/json/backgrounds.json').read())

    # 1) stats
    for i in range(6):
        char.stats.append(
            diceroll.roll('3d6')
        )

    # 1.1) background
    r = diceroll.roll() - 1
    char.background = backgrounds_data[r]
    
    # 2) ancestory
    r = diceroll.roll('d12')
    match r:
        case 1 | 2 | 3 | 4:
            char.ancestry = 'human'
        case 5 | 6:
            char.ancestry = 'elf'
        case 7 | 8:
            char.ancestry = 'dwarf'
        case 9 | 10:
            char.ancestry = 'halfling'
        case 11:
            char.ancestry = 'half-orc'
        case 12:
            char.ancestry = 'goblin'
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

    # 6) languages


    print('\n--CHARACTER--')
    print(f'Stats: {char.stats}')
    print(f'Background: {char.background}')
    print(f'Ancestry: {char.ancestry}')
    print(f'Class: {char.charclass}')
    print(f'Alignment: {char.alignment}')
    print(f'Title: {char.title}')
