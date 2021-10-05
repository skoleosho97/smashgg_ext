import discord
from discord.ext import commands
from discord_slash import SlashCommand, ComponentContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from data import constants

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=constants.prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_message(message):
    if message.author.bot or not message.guild:
        return

@bot.event
async def on_ready():
    print("Ready!")

#@slash.slash(name='setup',
 #            description='Setup a new game!',
  #           guild_ids=[constants.server])

@slash.slash(name='setcount',
             description='Find the set count of a specific player',
             guild_ids=[constants.server],
             options=[

             ])
async def setcount(ctx):
    return

bot.run(constants.token)