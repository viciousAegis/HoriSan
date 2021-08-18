import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild = self.bot.get_guild(id=840129026412904471)

        self.user = self.guild.get_member(835373517205012480)

    @commands.command()
    async def help(self, ctx):
        emb = discord.Embed(
            description=
            'these are the availible commands for hori\n\n> server prefix is `h!`\n\n[] are aliases of commands',
            color=discord.Color.from_rgb(241, 93, 147),
        )

        emb.set_author(name="Hori San - Help", icon_url=self.user.avatar_url)

        emb.add_field(
            name='*commands*',
            value='>>> `cute[qt]`\n`quote[q]`\n`dadjoke[dj]`\n`fact[f]`')

        emb.add_field(
            name='*confessions*',
            value=
            '>>> type `h!confess` in DM to confess (only applicable for SynCord)',
            inline=False)

        emb.add_field(name='*games*', value='>>> `tictactoe[t]`', inline=False)

        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Help(bot))
    print("---> HELP LOADED")
