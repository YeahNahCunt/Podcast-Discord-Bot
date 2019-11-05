import discord
from discord.ext import commands
import os #for bot token linking with host

client = commands.Bot(command_prefix = '|') #holder prefix change later

@client.event
async def on_ready():
    print('Bot is ready!')

client.run(os.environ['BOT_TOKEN'])
