import os
import discord
import requests
import json
import quotes
import traceback
from dadjokes import Dadjoke
from replit import db
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.all() 

client = commands.Bot(command_prefix = 'h!', case_insensitve = True, intents = intents)
client.remove_command("help")


def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
            except Exception as e:
                print(f"COG LOAD ERROR : {e}\n\n{traceback.format_exc()}\n\n")

@client.event
async def on_ready():

  load_cogs()

  game = discord.Game("with Miyamura")

  await client.change_presence(activity=game)
  
  print('Bot Ready')


@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! latency is {round(client.latency*1000)}ms')

@client.command(aliases = ['guilds','g'])
async def guild(ctx):
  guildNames = []

  guilds = client.guilds
  for guild in guilds:
    guildNames.append(guild.name)

  await ctx.send(f'{client.user.mention} is a member of {guildNames}')

@client.command(aliases = ['q'])
async def quote(ctx):
  quote = quotes.get_quote()
  await ctx.send(quote)

@client.command(aliases = ['dj'])
async def dadjoke(ctx):
  dadjoke = Dadjoke()
  await ctx.reply(dadjoke.joke)

keep_alive()
botToken = os.environ['token']
client.run(botToken)
