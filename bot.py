from discord.ext import commands
from constants import DISCORD_TOKEN


bot = commands.Bot(command_prefix='!')


@bot.command()
@commands.is_owner()
async def load(ctx, cog_name: str):
    try:
        bot.load_extension(cog_name)
    except Exception as err:
        await ctx.channel.send(f'**`{type(err).__name__} : {err}`**\U0001f62c')
    else:
        await ctx.channel.send(f"**Successfully loaded**: `{cog_name}`")


@bot.command()
@commands.is_owner()
async def unload(ctx, cog_name: str):
    try:
        bot.unload_extension(cog_name)
    except Exception as err:
        await ctx.channel.send(f'**`{type(err).__name__} : {err}`**\U0001f62c')
    else:
        await ctx.channel.send(f"**Successfully unloaded**: `{cog_name}`")


@bot.command()
@commands.is_owner()
async def reload(ctx, cog_name: str):
    try:
        bot.unload_extension(cog_name)
        bot.load_extension(cog_name)
    except Exception as err:
        await ctx.channel.send(f'**`{type(err).__name__} : {err}`**\U0001f62c')
    else:
        await ctx.channel.send(f"**Successfully reloaded**: `{cog_name}`")


bot.load_extension('cogs.utilities')
bot.load_extension('cogs.events')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.music')
bot.run(DISCORD_TOKEN)
