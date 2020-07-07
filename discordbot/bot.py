import discord
from discord.ext import commands
import os
from random import choice
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord...\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'like u' in message.content.lower() or 'like you' in message.content.lower():
        await message.channel.send("WAAPAS RAK")
    
    elif 'test' in message.content.lower() or 'exam' in message.content.lower():
        await message.channel.send('MITOSISAAAAA????')
    
    elif 'what' in message.content.lower() and 'cs' in message.content.lower():
        msg = choice(["Imblement da logik", "write a......BOOOOOOOOOLEAN EXPRESSION"])
        await message.channel.send(msg)

@bot.command(name = 'shutdown', help = 'shuts down the bot remotely')
async def shutdown(ctx):
    print('something')
    await ctx.send('ada paavi')
    await ctx.bot.logout()
    print("Bot has been shutdown by the command")

bot.run(token)