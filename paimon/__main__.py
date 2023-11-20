import settings
import discord
from discord.ext import commands

import settings
import rpgs.shadowdark.character as character
import diceroll
import models.paimondb as database

# intents that are needed
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# initialize the bot
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
)

# bot events go here
@bot.event
async def on_ready():
    print(f'User {bot.user} (ID: {bot.user.id}) is online.')

@bot.command(aliases=['gamemaster'])
async def gm(ctx):
    ...

@bot.command(aliases=['r'])
async def roll(ctx, dice = 'd20'):
    total = diceroll.roll(dice)
    await ctx.send(f'🎲 **{dice}:** {total}')

# ...finally, run the bot
bot.run(settings.TOKEN)
