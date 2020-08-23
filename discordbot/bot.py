import discord
from discord.ext import commands
import os
from random import choice
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
c_pandey = int(os.getenv('c_pandey'))

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord...\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('>'):
        return
    elif bot.user in message.mentions and ('are you x ae' in message.content.lower() or 'are you chulbul pandey' in message.content):
        await message.channel.send("Nahi sir, woh to mera judavaan bhai he sir.\nWoh Shyam, meh Ram...")
    elif message.content.lower() == 'ded':
        await message.channel.send("<a:coffin_dance:737353384595685377>")
    await bot.process_commands(message)
       
@bot.command(name = 'shutdown', help = 'shuts down the bot remotely',aliases = ['off','die','marana'])
async def shutdown(ctx):
    await ctx.channel.send("Understandable. Have a nice day ✌")
    await ctx.bot.logout()
    print(f"Bot has been shutdown by the command by {ctx.message.author.name}")

bot.run(token)
