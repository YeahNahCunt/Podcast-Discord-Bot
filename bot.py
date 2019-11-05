import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

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

##testing if online##
@client.command()
async def ping(ctx):
    await ctx.send(f'Surprise motherfucker in {client.latency * 1000}ms')


##VC Join##
@client.command(pass_context=True, aliases=['join', 'j', 'J'])
async def join_VC(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(chennel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(chennel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n') #console check

    await ctx.send(f'Joined {channel}')

##VC Leave##
@client.command(pass_context=True, aliases=['leave', 'l', 'L'])
async def leave_VC(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}\n') #console check
        await ctx.send(f'Left {channel}')
    else:
        print ('Bot was told to leave channel but not in one')
        await ctx.send('Í dont think im in a voice channel')

client.run(os.environ['BOT_TOKEN'])
