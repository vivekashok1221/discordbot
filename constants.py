import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

REDDIT_CLIENT_ID = os.getenv('reddit_client_id')
REDDIT_CLIENT_SECRET = os.getenv('reddit_client_secret')

RADIOS = {
        'HIFM': os.getenv('HiFM'),
        'MERGE': os.getenv('Merge'),
        'VIRGIN': os.getenv('Virgin')
        }

EMOJIS = {}
