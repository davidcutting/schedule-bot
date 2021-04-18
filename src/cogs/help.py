import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Help Menu',
            colour = 0xFFED86
        )
        embed.add_field(name = 'Help', value = 'This menu', inline = False)
        embed.add_field(name = 'Ping', value = 'Test ping of Bot', inline = False)

        await ctx.send(embed=embed)

def setup(client):
    client.remove_command('help')
    client.add_cog(Help(client))
