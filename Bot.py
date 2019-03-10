import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome in Official [A.N.A] ATLANTIDA discord for help write "-help"')
    print('Sent message to ' + member.name)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='with ATLANTIDA'))
    print('Bot Is Running Sucesfully')


async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))


@client.event
async def on_message(message):
    if message.content == '-web':
        await client.send_message(message.channel,'http://www.gck.clanweb.eu/')
    if message.content == '-cheers':
        em = discord.Embed(description='Cheers')
        em.set_image(url='https://cdn.discordapp.com/attachments/528194410924605440/529441936323510273/download_1.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('-coinflip'):
        randomlist = ["head", "tail", ]
        await client.send_message(message.channel, (random.choice(randomlist)))
    if message.content == '-help':
        await client.send_message(message.channel,'-web,-cheers,-coinflip')



async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))


client.run('NTU0MjQ4MzA0NTgyNDU5NDA3.D2Z4aA.VUBubYLveezRr0krh110z-GW_zI')
