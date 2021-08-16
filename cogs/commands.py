import random
import discord
import requests
import json
from discord.ext import commands,tasks

class Commands(commands.Cog):

  def __init__(self, client):
    self.client = client

    
  @commands.command(aliases = ['f'])
  async def fact(self,ctx):
    response = requests.get("https://useless-facts.sameerkumar.website/api")
    json_data = json.loads(response.text)
    fact = json_data['data']
    await ctx.send(fact)

  @commands.command(aliases = ["ct", "qt"])
  async def cute(self, ctx, mem: discord.Member=None):
    
    if mem == None:
      user = ctx.author
    else:
      user = mem

    cute = random.randint(0,100)

    img1 = "https://media1.tenor.com/images/8734763ade5ea8d88e587b5f0136f232/tenor.gif?itemid=21328454"

    img2 = "https://media1.tenor.com/images/ffa769a36fd1d52b65072b869a1cf40f/tenor.gif?itemid=21937672"

    desc = f'after contemplation, miyamura and i have made our decision!\n\n\n \t**{user.mention} has a cuteness rating of {cute}%!!**'

    emb = discord.Embed(
        title = "hori's cute-o-meter",
        color = discord.Colour.random(),
        description = desc,
        
    )

    emb.set_thumbnail(url = user.avatar_url)

    if cute < 50:
      emb.set_image(url=img1)
    else:
      emb.set_image(url=img2)

    await ctx.reply(embed = emb)

def setup(client):
    client.add_cog(Commands(client))
    print("---> COMMANDS LOADED")