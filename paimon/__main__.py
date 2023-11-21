import settings
import discord
from discord.ext import commands

import settings
import diceroll
from models.users import Users
import randomchar

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
    discord_id = ctx.message.author.id
    guild_id = ctx.message.guild.id

    user = Users.create(
        discord_id,
        guild_id,
    )
    user.save()

    await ctx.send('YOU ARE NOW THE GM!')

@bot.command(aliases=['r'])
async def roll(ctx, dice = 'd20'):
    total = diceroll.roll(dice)
    await ctx.reply(f'🎲 **{dice}:** {total}')

@bot.command()
async def char(ctx,
    random: int = 1,
):
    if random:
        randomchar.randomchar(ctx)

# ...finally, run the bot
bot.run(settings.TOKEN)
