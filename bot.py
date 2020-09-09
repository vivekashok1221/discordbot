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


@bot.command()
async def ping(ctx):
    await ctx.send(f"`ping:{round(bot.latency,2)}`")


bot.load_extension('cogs.music')
print("Music loaded.")

bot.run(TOKEN)
