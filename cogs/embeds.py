import discord
from discord.ext import commands, tasks
import json


class Embeds(commands.Cog):

    #WATER PING EMBED MAKER
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def wp(self, ctx):

        guild = ctx.guild
        emote = '🌊'
        role = guild.get_role(868030929975795712)

        message = 'React to this message to get notified about drinking water every 60 mins while you are studying!'

        emb = discord.Embed(title='Water Pings!',
                            description=message,
                            color=discord.Colour.blue())
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emote)

        with open("reactRoleData.json") as json_file:
            data = json.load(json_file)

            newReactRole = {
                'roleName': role.name,
                'roleID': role.id,
                'emote': emote,
                'msgID': msg.id
            }

            data.append(newReactRole)

        with open('reactRoleData.json', 'w') as j:
            json.dump(data, j, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lr(self, ctx):

        guild = ctx.guild
        emote = '📚'
        role = guild.get_role(870885281820192768)

        message = 'React to this message to **DISABLE** access to the study lounge while you are studying!'

        emb = discord.Embed(title='Lounge!',
                            description=message,
                            color=discord.Colour.blue())
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emote)

        with open("reactRoleData.json") as json_file:
            data = json.load(json_file)

            newReactRole = {
                'roleName': role.name,
                'roleID': role.id,
                'emote': emote,
                'msgID': msg.id
            }

            data.append(newReactRole)

        with open('reactRoleData.json', 'w') as j:
            json.dump(data, j, indent=4)


def setup(client):
    client.add_cog(Embeds(client))
    print("---> EMBEDS LOADED")
