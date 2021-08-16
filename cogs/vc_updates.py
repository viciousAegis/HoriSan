import discord
from discord.ext import commands, tasks

SERVER_ID = 840129026412904471
VIDEO_VC = 866248681022947328

STUDY_LOUNGE = 863473470246354954
LOFI_ROOM = 859401790449647677

class Study(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        

        self.GUILD =  self.bot.get_guild(id=840129026412904471)

        self.STUDY_CATEGORY = discord.utils.get(
          self.GUILD.categories, id = 840228111320481792
        )

        self.UPDATE_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=870977890353831976
        )

        self.STUDY_ROLE_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=870886015915675678
        )

        self.STUDY_ROLE = self.GUILD.get_role(854997618958925844)

        self.LOUNGE_ROLE = self.GUILD.get_role(870885281820192768)

        self.kick_stalkers.start()

        # self.update_count.start()

        

    @tasks.loop(seconds=60)
    async def kick_stalkers(self):
        # MOVE MEMBERS WHO DONT HAVE VIDEO OR SCREENSHARE
        guild_ = self.bot.get_guild(SERVER_ID)
        video_vc_ = guild_.get_channel(VIDEO_VC)
        lofi = guild_.get_channel(LOFI_ROOM)
        lounge = guild_.get_channel(STUDY_LOUNGE)

        for mem in video_vc_.members:
          if mem.bot:
            return
          if not mem.voice.self_video:
              await mem.move_to(channel=lofi)
              print(f"moved {mem}")
              await lounge.send(
                  f"{mem.mention} was moved to <#{lofi.id}>\n->They did not turn on video",
                  delete_after=90,
                )
    
    # @tasks.loop(seconds = 5)
    # async def update_count(self):
    #   self.STUDENTS = 0

    #   for vc in self.STUDY_CATEGORY.voice_channels:
        
    #       self.STUDENTS += len(vc.members)
    #   for vc in self.STUDY_CATEGORY.stage_channels:
        
    #       self.STUDENTS += len(vc.members)

    #   print(self.STUDENTS)
    #   print('----')

    #   string = str(self.STUDENTS) + 'studying'

    #   await self.UPDATE_CHANNEL.edit(name = string)

    #   print('edited')
    #   print('----')
    
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
      if(member.guild == self.GUILD):

        self.UPDATE_TEXT_CHANNEL = discord.utils.get(
            self.GUILD.text_channels, id=870977890353831976
        )

        await self.UPDATE_CHANNEL.send("--the bot added the role below--")

        await self.UPDATE_CHANNEL.send(f'{self.LOUNGE_ROLE.name} added to **{member}** as they joined VC')

        if member.bot or (before.channel == after.channel):
          return

      
        if after.channel != None: # WHEN SOMEONE JOINS A STUDY CHANNEL
          if after.channel.category_id == self.STUDY_CATEGORY.id:

            await member.add_roles(self.LOUNGE_ROLE)

            
        elif after.channel == None:
          # WHEN SOMEONE LEAVES A STUDY CHANNEL
          if before.channel.category_id == self.STUDY_CATEGORY.id:

            if self.LOUNGE_ROLE in member.roles:
              await member.remove_roles(self.LOUNGE_ROLE)
              

              message = await self.STUDY_ROLE_CHANNEL.fetch_message(871075537739714580)
              reaction = message.reactions[0]

              
              await reaction.remove(member)

              await self.UPDATE_CHANNEL.send("--the bot removed the role below--")
              await self.UPDATE_CHANNEL.send(f'{self.LOUNGE_ROLE.name} removed from **{member}** as they left VC')

          else:
              pass
  


def setup(bot):
    bot.add_cog(Study(bot))
    print("---> VC UPDATES LOADED")