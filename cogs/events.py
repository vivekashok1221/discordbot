import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name='Bade Admin')
        await member.add_roles(role)
    # TODO: on ready uptime, error


def setup(bot):
    bot.add_cog(Events(bot))
    print("Added event cog")
