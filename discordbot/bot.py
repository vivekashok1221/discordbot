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
        print('ignored quote')
        return
    
    if message.content.lower() == '!shutdown':
        if message.author.name == 'EG Vivek':
            print("paavi")
            await message.channel.send("Ada paavi")
            await bot.logout()
        else:
            await message.channel.send("!sHuTdOwN.......lmao nooooob")
            #await message.channel.send(f"poda {message.author.name}")
 
    elif bot.user in message.mentions:
        c_pan = bot.get_user(c_pandey)
        await message.channel.send(f"X ae  badnaam hui, darling {c_pan.mention} liye... ")
        
    elif 'goodnight ujjwal' in message.content.lower():
        for i in range(5):
            await message.channel.send("goodnight ujjwal")
        
    elif 'like u' in message.content.lower() or 'like you' in message.content.lower():
        await message.channel.send("WAAPAS RAK")

    elif 'ded' in  message.content.lower()or 'dead' in message.content.lower():
        await message.channel.send("https://tenor.com/bioro.gif")
    
    elif 'test' in message.content.lower() or 'exam' in message.content.lower():
        await message.channel.send('MITOSISAAAAA????')
    
    elif 'what' in message.content.lower() and 'cs' in message.content.lower():
        msg = choice(["Imblement da logik", "write a......BOOOOOOOOOLEAN EXPRESSION"])
        await message.channel.send(msg)

        
#@bot.command(name = 'shutdown', help = 'shuts down the bot remotely')
#async def shutdown(ctx):
    #print('something')
    #await ctx.send('ada paavi')
    #await ctx.bot.logout()
    #print("Bot has been shutdown by the command")

bot.run(token)
