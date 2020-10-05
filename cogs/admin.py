import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            if ctx.command.name == "shutdown":
                await ctx.channel.send(
                    "You do not have the required permissions "
                    "<:abeysaale:731486907208433724>")


    @commands.command()
    async def emojis(self, ctx):
        for emoji in ctx.guild.emojis:
            if emoji.animated:
                await ctx.channel.send(f"a:{emoji.name}:{emoji.id}")

    @commands.has_permissions(administrator=True)
    @commands.command(help='shuts the bot down', aliases=['off', 'die'])
    async def shutdown(self, ctx):
        await ctx.channel.send("Understandable. Have a nice day ✌")
        await self.bot.logout()
        print(f"Bot has been shut down by {ctx.message.author.name}")

    @commands.command()
    @commands.is_owner()
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *reason):
        reason = ' '.join(reason)
        mute_role = discord.utils.get(ctx.guild.roles, name='mute')
        await member.add_roles(mute_role, reason=reason)
        await ctx.channel.send(
                            "<a:crab_rave:753654717506256937> "
                            f"{member.mention} has been muted "
                            "<a:crab_rave:753654717506256937>")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name='mute')
        await member.remove_roles(mute_role)
        await ctx.channel.send(f"{member.mention} has been **unmuted**")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *reason):
        reason = " ".join(reason) if reason != () else "unspecified"
        embed = discord.Embed(
                            title=f"You have been kicked from {ctx.guild}",
                            description=f"reason: {reason}")
        await ctx.channel.send(
                            f"{member.mention} has been **kicked** "
                            "<a:cat_vibing:753973817608634468>\n**"
                            f"`reason:` **{reason}")
        
        try:                    
            await member.send(embed=embed)
        except:
            raise
        finally:
            await member.kick(reason=reason)

    # TODO: channel specific mute


def setup(bot):
    bot.add_cog(Admin(bot))
    print("Added Admin cog")
