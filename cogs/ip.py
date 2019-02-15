import discord
from discord.ext import commands

#ip command
class ip:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx):
        await ctx.send('play.SkySpaceMc.net')

#info command
class info:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='**Server ip:**', value='\n   -play.SkySpaceMc.net \n', inline=True)
        embed.add_field(name='**Website:**', value='   -coming soon... \n', inline=True)
        embed.add_field(name='**Store:**', value='   -http://sky-space.buycraft.net/ \n', inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ip(bot))
    bot.add_cog(info(bot))