import random
from parsy import regex, string, seq

def parse(s: str):
    number = regex(r'[0-9]*')
    d = string('d') | string('D')
    plus = string('+')

    # commands do not allow whitespace!
    dice = seq(
        number.optional(),
        d,
        number,
        # if there's a plus the number, then all below is required
        seq(
            plus,
            number
        ).optional()
    )

    return dice.parse(s)

def roll(d: str):
    total = 0
    parsed = parse(d)

    roll = 0
    if parsed[0]:
        for _ in range(0, int(parsed[0])):
            roll = random.randint(1, int(parsed[2]))
            total += roll
    else:
        total = random.randint(1, int(parsed[2]))
    
    if parsed[3]:
        total += int(parsed[3][1])

    return total

'''
print(
    parse('1d20+')
)
'''