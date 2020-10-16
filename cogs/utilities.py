import discord
from discord.ext import commands


class Utilities(commands.Cog):
    '''Commands that are useful for the users'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"`ping:{round(self.bot.latency,2)}`")

    @commands.command()
    async def bookmark(self, ctx, target: discord.Message, *comments):
        comments = ' '.join(comments) if len(comments) != 0 else None
        embed = discord.Embed(
            title="DID SOMEONE TYPE  !bookmark ???",
            color=discord.Colour.gold())
        embed.set_author(name=target.author, icon_url=target.author.avatar_url)
        embed.add_field(
            name="Well, here ya go:",
            value=f"link to [message]({target.jump_url})")
        try:
            user_embed = embed.copy()
            user_embed.description = target.content
            if comments:
                embed.add_field(
                    name="comments:",
                    value=comments)
            await ctx.author.send(embed=user_embed)

        except discord.Forbidden:
            user_embed.set_colour = discord.Colour.red()
            embed.set_footer(
                text="Can't send bookmark to user "
                "as DMs are disabled.")
        else:
            embed.set_footer(
                text="Bookmark has been sent to "
                f"{ctx.author}'s DM")
        finally:
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utilities(bot))
    print("Added untilites cog")
