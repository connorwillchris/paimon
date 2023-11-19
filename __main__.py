import settings
import discord
from discord.ext import commands

import random

import rpgs.shadowdark.character as character
import diceroll

def run():
    intents = discord.Intents.default()

    # intents that are needed
    intents.message_content = True

    bot = commands.Bot(
        command_prefix='!',
        intents=intents,
    )

    @bot.event
    async def on_ready():
        print('Paimon is online.')
        c = character.randchar()
    
    @bot.command(
        aliases=['r'],
    )
    async def roll(ctx, dice):
        total = 0
        if dice:
            total = diceroll.roll(dice)
        await ctx.send(f'🎲 **{dice}:** {total}')

    @bot.command()
    async def randchar(ctx):
        character.randchar(ctx)

    bot.run(settings.TOKEN)

# run the bot
run()
