#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import os
import discord
from Private import discord_app
from DISCORD.DELETE import delete_chat
from DISCORD.BARCODE import double_barcode_check
from DISCORD.ELOUNDA import elounda
from DISCORD.INTERNET import internet
from DISCORD.PDA import pda
from DISCORD.THALASSINA import thalassina_app
from DISCORD.KEROULIS import keroulis
from DISCORD.MANAVIKI import manaviki
from DISCORD.PAGOTA import pagota
from DISCORD.DELTA import delta
from DISCORD.ORDER import new_order
from DISCORD.BAZAAR import bazaar
from DISCORD.VARDAS import vardas

TOKEN = discord_app.token()
GUILD = os.getenv(discord_app.guild())

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # (-) (+) DAILY -------------------------------------------------------
    if message.content.lower() == 'd1':
        delete_chat.run(1)
        double_barcode_check.run()
        elounda.run()
        internet.run()
        pda.run()
        thalassina_app.run()
        keroulis.run()
        manaviki.run()
        pagota.run()
        delta.run()
        response = 'DAILY ΕΝΗΜΕΡΩΣΕΙΣ: COMPLETE'
        await message.channel.send(response)

    # (-) (+) MONTHLY -------------------------------------------------------
    if message.content.lower() == 'm1':
        delete_chat.run(4)
        vardas.run()
        response = 'MONTHLY ΕΚΚΡΕΜΟΤΗΤΕΣ: COMPLETE'
        await message.channel.send(response)

    # (-) ORDERS -------------------------------------------------------
    if message.content.lower() == '-order':
        delete_chat.run(3)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΑΡΑΓΓΕΛΙΕΣ: COMPLETE'
        await message.channel.send(response)

    # (+) ORDERS -------------------------------------------------------
    if message.content.lower().split(' ')[0] == '+order':
        new_order.run(message.content.split(' ')[1])
        response = 'ΚΑΤΑΧΩΡΗΣΗ ΠΑΡΑΓΓΕΛΙΑΣ: COMPLETE'
        await message.channel.send(response)

    # (-) (+) BAZAAR -------------------------------------------------------
    if message.content.lower() == 'bazaar':
        delete_chat.run(5)
        bazaar.run()
        response = 'ΚΑΤΑΧΩΡΗΣΗ ΤΙΜΟΛΟΓΙΩΝ BAZAAR: COMPLETE'
        await message.channel.send(response)


client.run(TOKEN)
