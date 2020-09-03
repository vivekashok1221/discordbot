import asyncio
import discord
from discord.ext import commands
import os
from random import choice
import youtube_dl
from youtube_search import YoutubeSearch

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord...\n")

@bot.event
async def on_message(message):
    if 'wiggle' in message.content.lower():
        await message.delete()
    if 'https://discord.gg' in message.content:
        await message.delete()
    await bot.process_commands(message)

class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.voice = None
        
    @commands.command()
    async def poem(self,ctx):  #TODO: add poems
        await ctx.channel.send('''*clears throat*
        My daddy cry if I fail ...
        then I hit you and go to jail ... 
        but don't worry I get easy bail ... 
        then I again hit you, again jail, again bail ... 
        then jail bail, jail bail, jail bail ... 
        and one day your heart fail''')

    @commands.command(aliases = ['j','aaja'])
    async def join(self,ctx):
        self.playlist = []
        # playlist = asyncio.Queue()
        try:
            await ctx.message.author.voice.channel.connect()
            await ctx.channel.send('**Meh raazi! Tu raazi! `Connected to your VC`**')
            self.voice = ctx.message.guild.voice_client
        except:
            if self.voice:
                await ctx.channel.send('**Arree BC, I\'m already connected to a VC**')
            else:
                await ctx.channel.send('**Meh raazi, lekin Tu nahi raazi. `Please connect to a VC first.`**')

    def next(self,ctx):
        if len(self.playlist) > 0:
            self.url_ = self.playlist.pop(0)
            asyncio.run_coroutine_threadsafe(self.play(ctx,self.url_),self.bot.loop)

    @commands.command()
    async def play(self,ctx,*args): #TODO: check if user is connected to VC

        def play_(url):
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(url,download=False )
                stream_url = result['formats'][0]['url'] 
            before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"    
            self.voice.play(discord.FFmpegPCMAudio(stream_url,before_options=before_options),after =lambda e: self.next(ctx))
            
        self.song = ' '.join(args)
        YTresults = YoutubeSearch(self.song, max_results=1).to_dict()
        for result in YTresults:
            url_ = 'https://www.youtube.com'+ result['url_suffix']
        self.playlist.append(url_)

        if self.voice.is_playing():
            await ctx.channel.send('added to queue')
            return
            #TODO: add to queue
        else:
            self.url_ = self.playlist.pop(0)
            play_(self.url_)
            await ctx.channel.send(f"\U0001f4c0`Aapko Sunaana Chaahta Hoon:`\U0001f4c0\n{self.url_}")
            
    

    @commands.command(name = 'pause',aliases = ['rokku'])
    async def pause_(self,ctx): #TODO: checking
        self.voice.pause()
        await ctx.channel.send("*Me karu intezer tera...* `Song has been paused` \u23f8")


    @commands.command(name = 'resume')
    async def resume_(self,ctx):
        await ctx.channel.send("*RESUMING bhai...*\u23ef")
        self.voice.resume()

    @commands.command()
    async def skip(self,ctx):
        if self.playlist or self.voice.is_playing():
            await ctx.channel.send("**`song skipped`** \U0001fa93")
        else:
            await ctx.channel.send("No songs to skip")
        self.voice.stop()

    @commands.command(aliases = ['r'])
    async def remove (self,ctx,position : int):
        if position < 0:
            self.playlist.pop(position)
        else:self.playlist.pop(position-1)
        await ctx.channel.send("removed")
    
    
    @commands.command(aliases = ['m'])
    async def move(self,ctx,initial:int,final : int = 0):
        s =self.playlist.pop(initial-1)
        self.playlist.insert(final-1,s)
        await ctx.channel.send(f"moved to {final}")
        del s

    @commands.command(name = 'clear')
    async def clear_(self,ctx):
        self.playlist.clear()
        await ctx.channel.send("`Queue has been cleared`")

    @commands.command(name = 'queue',aliases = ['q','ganas'])
    async def listqueue(self,ctx):
        plals = str(self.playlist)
        await ctx.channel.send(plals)


    @commands.command(help = f"Disconnects from Voice Channel", aliases = ['d'])
    async def disconnect(self,ctx):
        await self.voice.disconnect()
        await ctx.channel.send('**Tumhari mansik isthithi aaj thodi gadbad lag rahi hai ... hum baad mein phir aayenge**\n`Disconnected from VC `')
        self.playlist.clear()


@bot.command(name = 'shutdown', help = 'shuts down the bot remotely',aliases = ['off','die','marana'])
async def shutdown(ctx):
    await ctx.channel.send("Understandable. Have a nice day ✌")
    await ctx.bot.logout()
    print(f"Bot has been shutdown by the command by {ctx.message.author.name}")


@bot.command(name = 'purge')
@commands.is_owner() 
async def purge(ctx,limit : int):
    await ctx.channel.purge(limit=limit+1)

#@bot.command(name = 'leavethisserver')
#async def leave_(ctx):
    #await ctx.channel.send("Understandable. Have a nice day ✌")
    #await ctx.guild.leave() 

@bot.command()
async def ping(ctx):
    await ctx.send(f"`ping:{round(bot.latency,2)}`")

bot.add_cog(Music(bot))
bot.run(token)
