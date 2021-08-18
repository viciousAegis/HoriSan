
import discord
from discord.ext import commands, tasks
import json

class ReactionRole(commands.Cog):

  def __init__(self, client):
    self.client = client
    
    self.GUILD = self.client.get_guild(id=840129026412904471)

    self.STUDY_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=863473470246354954
        )

    self.STUDY_ROLE_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=870886015915675678
        )
    
    self.STUDY_ROLE = self.GUILD.get_role(854997618958925844)

    self.LOUNGE_ROLE = self.GUILD.get_role(870885281820192768)

    self.UPDATE_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=870977890353831976
        )

    # self.wotah_pings.start()

  @commands.Cog.listener()
  async def on_ready(self):
    
    print('bot ready')


#REACTION ROLE ADDING
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):

    if payload.guild_id == None:
      return

    member = payload.member

    if member.bot:
      return

    with open('reactRoleData.json') as j:
      data = json.load(j)

      for x in data:
        
        if x['emote'] == payload.emoji.name and x['msgID'] == payload.message_id:

          role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

          if(role.name == 'Lounging'): 
            

            # if(self.STUDY_ROLE not in member.roles):
              
            #   await self.STUDY_ROLE_CHANNEL.send(
            #     f'{member.mention}, you require the {self.STUDY_ROLE.mention} role in order to get this role. you can get this role by joining a study vc',
            #     delete_after = 60,
            #     )

            #   message = await self.STUDY_ROLE_CHANNEL.fetch_message(payload.message_id)
            #   reaction = message.reactions[0]

            #   await self.UPDATE_CHANNEL.send("--the bot removed the role below--")
            #   await reaction.remove(member)

            #   break


            await self.UPDATE_CHANNEL.send(f'{role.name} was removed from **{member}**')

            await member.remove_roles(role)
          else:
            await self.UPDATE_CHANNEL.send(f'{role.name} was given to **{member}**')

            await member.add_roles(role)

  #REACTION ROLE REMOVING
  @commands.Cog.listener()

  async def on_raw_reaction_remove(self, payload):
    
    if payload.guild_id == None:
      return

    member = self.client.get_guild(payload.guild_id).get_member(payload.user_id)

    with open('reactRoleData.json') as j:
      data = json.load(j)

      for x in data:
        
        if x['emote'] == payload.emoji.name and x['msgID'] == payload.message_id:

          role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

          if(role.name == 'Lounging'):

            await self.UPDATE_CHANNEL.send(f'{role.name} was given to **{member}**')

            await member.add_roles(role)

          else:
            await self.UPDATE_CHANNEL.send(f'{role.name} was removed from **{member}**')

            await member.remove_roles(role)
  #----------------------------------------------


  #WATER PINGING LOOP



  @tasks.loop(minutes = 60)
  async def wotah_pings(self):
    
    ping_role_id = 868030929975795712

    hist = await self.STUDY_CHANNEL.history(oldest_first=False, limit=250).flatten()
    for message in hist:
      if (
        message.author.id == self.client.user.id
        and str(ping_role_id) in message.content
      ):
        await message.delete()

    await self.STUDY_CHANNEL.send(f"<@&{ping_role_id}> its time to drink!")


def setup(client):
    client.add_cog(ReactionRole(client))
    print("---> ROLES LOADED")
