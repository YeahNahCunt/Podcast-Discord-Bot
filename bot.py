import discord
from discord.ext import commands
import os #for bot token linking with host

client = commands.Bot(command_prefix = '|') #holder prefix change later

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Suck ya mum'))
    print('Bot is ready!')
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('*******************')

@client.command()   #for testing
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f'Surprise motherfucker in {client.latency * 1000}ms')

client.run(os.environ['BOT_TOKEN'])
