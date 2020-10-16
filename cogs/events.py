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

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} has connected to discord...\n")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print("hmmmm")
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send("You are missing some arguments...")
        elif isinstance(error, commands.BadArgument):
            await ctx.channel.send("Try again. Bad arguments supplied.")
        elif (cog := ctx.cog):
            if cog.qualified_name == "Music" \
                    and isinstance(error, commands.CheckFailure):
                return

        bot_channel = discord.utils.get(ctx.guild.channels, name="bot-updates")
        embed = discord.Embed(
                            title="Uh-oh...",
                            description=f"{type(error).__name__} : {error}",
                            colour=discord.Colour.red()
                            )
        await bot_channel.send(f"{ctx.author.mention}", embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
    print("Added event cog")
