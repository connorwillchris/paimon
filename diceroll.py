import random

def roll(d: str = 'd20'):
    total = 0
    v = None
    try:
        v = d.split('d')
    except:
        print('The following command does not include a \'d\'!')

    if v[0] == '':
        v[0] = 1

    for _ in range(int(v[0])):
        roll = random.randint(1, int(v[1]))
        total += roll

    return total
