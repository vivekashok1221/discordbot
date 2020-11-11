from discord.ext import commands
from constants import DISCORD_TOKEN


bot = commands.Bot(command_prefix='!')


extensions = (
    'cogs.ext',
    'cogs.utilities',
    'cogs.events',
    'cogs.admin',
    'cogs.music')
ignored_extensions = ('cogs.music', )  # extensions not to be loaded

if __name__ == '__main__':
    for extension in extensions:
        if extension not in ignored_extensions:
            bot.load_extension(extension)
    print('Loaded all extensions')
    bot.run(DISCORD_TOKEN)
