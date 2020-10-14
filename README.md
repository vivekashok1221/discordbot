# Humpty Sharma (A python Discord Bot)
Hi I'm Humpty Sharma! I'm a a multipurpose discord bot and I can perform various functions such as playing music, moderation etc! My creator is working on adding new features
daily! If you're wondering, my name is modelled after the character of the same name from the bollywoood movie Humpty Sharma ki Dulhania.
I don't speak Hindi and had to take help of google translate. If there are any mistakes, please let me know.

# How to run it
- If you wish to host the bot yourself, install the required depedencies by running ```pip install -r requirements.txt```

- Create a file name ```.env``` in the root folder of the project and mention your bot token in it.
it will look something like this:
```
#.env
DISCORD_TOKEN = YourBotToken
```
A bot token can be acquired by creating an application and adding bot at [Discord Developer Portal](https://discord.com/developers/applications).

- Run the bot by typing `python bot.py` in terminal/CMD.

- If you want to add more cogs, add them to /cogs/ and don't forget to load it in bot.py.

##### Dependancies Required
- [discord.py>=1.3.4](https://pypi.org/project/discord.py/)
- [PyNaCl>=1.4.0](https://pypi.org/project/PyNaCl/)
- [python-dotenv>=0.14.0](https://pypi.org/project/python-dotenv/)
- [youtube-dl>=2020.7.28](https://pypi.org/project/youtube_dl/)
- [youtube-search>=1.1.0](https://pypi.org/project/youtube-search/)

For installation of libraries and for further information click on the Dependancy Tag which will redirect you to the respective Python Documentation

# Humpty Sharma Features and Commands
## Admin Commands:
- ```mute/unmute``` - mutes/unmutes the specified user
- ```kick``` - kicks the specified user
- ```shutdown``` - shuts down the bot
- ```purge``` - deletes the specified number of messages in that particular channel

## Music Commands:
- ```join``` - summons the bot to the user's voice channel
- ```play``` - plays the song from the given name or url
- ```radio``` - streams one of the radio station: 95.9HiFM, Merge104.8 or 100.9VirginRadio based on user input
- ```pause``` - pauses the current playing song
- ```resume``` - resumes the paused song
- ```skip``` - skips the current playing song
- ```repeat``` - repeats the current playing song once
- ```remove``` - removes a particular song from the queue
- ```move``` - moves a song from a particular position in the queue to the specified position
- ```clear``` - clears the queue
- ```queue``` - displays the queue of songs to be played next in order
- ```nowplaying``` - displays the current playing song
- ```disconnect``` - disconnects the bot from the voice channel it was connected to

## Utilities:
- ```bookmark``` - bookmarks a message and sends user the message link in DMs

## Extra:
- ```load``` - for manually loading a cog
- ```unload``` - for manually unloading a cog
- ```reload``` -for manually reloading a cog

## Soon:
- `search` command for the Music cog
- `seek` command for the Music cog
- various commands that give information about the user and the server for the Utilities cog
- `Games`cog
