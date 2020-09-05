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


def active_voice(ctx):
    voice = ctx.message.author.voice
    if (voice.channel != None and  ctx.message.guild.voice_client.channel == voice.channel
        and not voice.self_deaf and not voice.deaf):
            return True
    
    return ctx.author == ctx.guild.owner


class Song:
    def __init__(self,url,stream_url,title,duration,requestor):
        self.url = url
        self.stream_url = stream_url
        self.title = title
        self.duration = duration        
        self.requestor = requestor


class Music(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.voice = None
        self.currentsong = None

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


    def playsong(self,ctx):
        '''Master play function'''
        if len(self.playlist) > 0:
            self.currentsong = self.playlist.pop(0)
            
            before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"    
            self.voice.play(
                            discord.FFmpegPCMAudio(self.currentsong.stream_url,before_options=before_options),
                            after =lambda e: self.playsong(ctx)
                            )            
            asyncio.run_coroutine_threadsafe(ctx.channel.send(f"\U0001f4c0`Aapko Sunaana Chaahta Hoon:`\U0001f4c0\n{self.currentsong.url}"),self.bot.loop)
    
    
    @commands.command()
    @commands.check(active_voice)
    async def play(self,ctx,*args):
        
        searchquery = ' '.join(args)

        YTresults = YoutubeSearch(searchquery, max_results=1).to_dict()
        for result in YTresults:
            url_ = 'https://www.youtube.com'+ result['url_suffix']
            title = result.get('title')
            duration = result.get('duration')
        
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url_,download=False)
            stream_url = result['formats'][0]['url']

        if self.voice.is_playing():
            await ctx.channel.send(f'`{title}` has been added to queue')
            songObj = Song(url_,stream_url,title,duration, ctx.message.author) 
            self.playlist.append(songObj)
            return
        else:
            songObj = Song(url_,stream_url,title,duration, ctx.message.author) # repeating is faster
            self.playlist.append(songObj)
            self.playsong(ctx)
            
    
    
    @commands.command(name = 'pause',aliases = ['rokku'])
    @commands.check(active_voice)
    async def pause_(self,ctx):
        '''Pauses the current playing song'''
        self.voice.pause()
        await ctx.channel.send("*Me karu intezer tera...* `Song has been paused` \u23f8")


    @commands.command(name = 'resume')
    @commands.check(active_voice)
    async def resume_(self,ctx):
        '''Resumes the paused song'''
        await ctx.channel.send("*RESUMING bhai...*\u23ef")
        self.voice.resume()


    @commands.command(aliases = ['s','hutt'])
    @commands.check(active_voice)
    async def skip(self,ctx):
        if self.voice.is_playing():
            await ctx.channel.send("**`song skipped`** \U0001fa93")
        else:
            await ctx.channel.send("No songs to skip\U0001f926")
        self.voice.stop()


    @commands.command(aliases = ['r'])
    @commands.check(active_voice)
    async def remove (self,ctx,position : int):
        '''Removes song at position from queue'''
        if self.playlist:
            if position < 0:
                s =self.playlist.pop(position)
            else:
                s = self.playlist.pop(position-1)
            await ctx.channel.send(f"**removed `{s.title}` from the queue**") #TODO: emoji
            del s
    
    
    @commands.command(aliases = ['m'])
    async def move(self,ctx,initial:int,final : int = 1):
        '''Moves position of song from the specified intial position to final position'''

        if initial < 1 or final < 1:
            await ctx.channel.send("`Invalid Arguments, naughty boy`")
            return
        s =self.playlist.pop(initial-1)
        self.playlist.insert(final-1,s)
        await ctx.channel.send(f"**`{s.title}` moved to position {final}** \u2705")
        del s


    @commands.command(name = 'clear')
    @commands.check(active_voice)
    async def clear_(self,ctx):
        self.playlist.clear()
        await ctx.channel.send("`Queue has been cleared`\u2705")


    @commands.command(name = 'queue',aliases = ['q','gaanas'])
    async def listqueue(self,ctx):
        '''List the songs in queue'''

        if self.playlist:
            embed = discord.Embed(title = 'Yeh hei tera queue:',colour = discord.Colour.gold())
            embed.description = f'Now Playing: {self.currentsong.title}\n\n'
            for song in self.playlist:
                embed.add_field(name = song.title,value = f'Requested by: {song.requestor}\nDuration: {song.duration}', inline = False)
        else:
            embed = discord.Embed(title = 'Abbe...',description = "Queue is empty",colour = discord.Colour.red())

        await ctx.channel.send(embed = embed)


    @commands.command(help = f"Disconnects from Voice Channel", aliases = ['dis'])
    @commands.check(active_voice)
    async def disconnect(self,ctx):
        await self.voice.disconnect()
        await ctx.channel.send('**Tumhari mansik isthithi aaj thodi gadbad lag rahi hai ... hum baad mein phir aayenge**\n`Disconnected from VC`')
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
