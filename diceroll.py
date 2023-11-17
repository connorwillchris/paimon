import random

def roll(d: str):
    total = 0
    v = d.split('d')

    if v[0] == '':
        v[0] = 1

    for _ in range(int(v[0])):
        roll = random.randint(1, int(v[1]))
        total += roll

    return total
