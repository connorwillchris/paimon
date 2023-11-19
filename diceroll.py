import random

from parsy import regex, string, seq, eof

def parse(s: str):
    number = regex(r'[1-9][0-9]*')
    d = string('d') | string('D')
    plus = string('+')
    spaces = string(' ')

    dice_format = seq(
        number.optional(),
        d,
        number,
        spaces.optional(),
        # if there's a plus the number below is required
        seq(
            plus,
            spaces.optional(),
            number
        ).optional()
    )

    return dice_format.parse(s)

def roll(d = '1d20'):
    total = 0
    parsed = parse(d)

    roll = 0
    if parsed[0]:
        for _ in range(0, int(parsed[0])):
            roll = random.randint(1, int(parsed[2]))
            total += roll
    else:
        total = random.randint(1, int(parsed[2]))
    
    if parsed[4]:
        total += int(parsed[4][2])

    return total

'''
print(
    parse('1d20+')
)
'''