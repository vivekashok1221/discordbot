from discord.ext import commands


class Extensions(commands.Cog):
    '''Cog for managing extensions'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog_name: str):
        try:
            self.bot.load_extension(cog_name)
        except Exception as err:
            await ctx.channel.send(f'**`{type(err).__name__} : {err}`**')
        else:
            await ctx.channel.send(f"**Successfully loaded**: `{cog_name}`")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog_name: str):
        try:
            self.bot.unload_extension(cog_name)
        except Exception as err:
            await ctx.channel.send(f'**`{type(err).__name__} : {err}`**')
        else:
            await ctx.channel.send(f"**Successfully unloaded**: `{cog_name}`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog_name: str):
        try:
            self.bot.unload_extension(cog_name)
            self.bot.load_extension(cog_name)
        except Exception as err:
            await ctx.channel.send(f'**`{type(err).__name__} : {err}`**')
        else:
            await ctx.channel.send(f"**Successfully reloaded**: `{cog_name}`")


def setup(bot):
    bot.add_cog(Extensions(bot))
    print("Added extensions cog")
