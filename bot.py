import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord...\n")


@bot.event
async def on_command_error(ctx, error):
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


@bot.command()
async def ping(ctx):
    await ctx.send(f"`ping:{round(bot.latency,2)}`")


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

        
bot.load_extension('cogs.events')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.music')
bot.run(TOKEN)
