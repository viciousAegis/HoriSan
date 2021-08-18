import discord
from discord.ext import commands


class Confession(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.confesser = None
        self.accept = "✅"

        self.deny = "❎"

        self.msg = None

        self.GUILD =  self.bot.get_guild(id=840129026412904471)

        self.CHANNEL = self.GUILD.get_channel(866509476101881886)

    @commands.command()
    async def confess(self, ctx, *, conf=None):

        if ctx.author.bot:
            return

        if ctx.guild != None:
            await ctx.send(
                'please use this command only through Direct Message'
                )
            return
        
        self.confesser = ctx.author

        

        if conf == None:
          await ctx.send("the command is as follows:")
          await ctx.send('> **h!confess <your confession here>**')
          
          return

        await ctx.send(f'are you sure you want to send this confession? this is what it will look like:')

        self.emb = discord.Embed(
          title = 'SynCord Confessions',
          description = f'"{conf}"',
          color = discord.Color.random()
        )
        
        self.msg = await ctx.send(embed = self.emb)

        await self.msg.add_reaction(self.accept)
        await self.msg.add_reaction(self.deny)
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

      if reaction.message.guild != None:
        return

      
      if user.bot:
        return


      if user == self.confesser:
        
        if reaction.message.id == self.msg.id:

          if reaction.emoji == self.deny:
            await self.msg.channel.send('confession cancelled')
            
          elif reaction.emoji == self.accept:
            await self.msg.channel.send('> sending...')
            await self.CHANNEL.send(embed = self.emb)
            await self.msg.channel.send('> sent!~')

          await self.msg.delete()




def setup(bot):
    bot.add_cog(Confession(bot))
    print("---> CONFESSIONS LOADED")
