import discord
import os
from itertools import cycle
from discord.ext import commands, tasks
from pip._vendor import requests

bot = commands.Bot(command_prefix = '-')
bot.remove_command('help')

@bot.event
async def on_connect():
    print('Connected to Discord')



for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')


async def change_status():
    await bot.change_presence(status= discord.Status.idle())

    
@bot.event
async def on_ready():
    change_status.start()
    print('<------------------------------>')
    print('EPAX\'s Bot is ready')
    print(f'Using Discord.py Version {discord.__version__}')
    print('<------------------------------>')

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CheckFailure):
    embed = discord.Embed(title = ':x: oops! You do not have permission to use this command.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error,commands.MissingRequiredArgument):
    embed = discord.Embed(title = ':x:You are missing the required arguements. Please check if your command requires an addition arguement.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error, commands.CommandNotFound):
    pass

bot.run('TOKEN HERE')

