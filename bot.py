import discord
from discord.ext import commands
import os #for bot token linking with host

client = commands.Bot(command_prefix = '|') #holder prefix change later

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Suck ya mum')
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

client.run(os.environ['BOT_TOKEN'])
