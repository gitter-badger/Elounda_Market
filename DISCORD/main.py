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
from DISCORD.ORDER import new_order, check_available_order
from DISCORD.BAZAAR import bazaar
from DISCORD.VARDAS import vardas
from DISCORD.PRE_COST_CALCULATION import pre_cost_calc
from DISCORD.PENDING import pendings
from DISCORD.PRICE_HISTORY import price_history

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
    if message.content.lower().startswith('refresh daily'):
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
    if message.content.lower().startswith('refresh monthly'):
        delete_chat.run(4)
        pendings.run()
        vardas.run()
        response = 'MONTHLY ΕΚΚΡΕΜΟΤΗΤΕΣ: COMPLETE'
        await message.channel.send(response)

    # (CHECK) ORDERS -------------------------------------------------------
    if message.content.lower().startswith('orders?'):
        response = check_available_order.run()
        await message.channel.send(response)

    # (-) ORDERS -------------------------------------------------------
    if message.content.lower().startswith('delete orders'):
        delete_chat.run(3)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΑΡΑΓΓΕΛΙΕΣ: COMPLETE'
        await message.channel.send(response)

    # (+) ORDERS -------------------------------------------------------
    if message.content.lower().startswith('add order'):
        try:
            order_id = message.content.split(' ')[2]
        except IndexError:
            await message.channel.send('Η ΣΥΝΤΑΞΗ ΤΗΣ ΕΝΤΟΛΗΣ ΕΙΝΑΙ: {add order + __code__}')
            return
        new_order.run(order_id)
        response = f'ΚΑΤΑΧΩΡΗΣΗ ΠΑΡΑΓΓΕΛΙΑΣ {order_id}: COMPLETE'
        await message.channel.send(response)

    # (-) PRE COST CALC -------------------------------------------------------
    if message.content.lower().startswith('delete pre cost'):
        delete_chat.run(6)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΡΟ ΚΟΣΤΟΛΟΓΗΣΗ: COMPLETE'
        await message.channel.send(response)

    # (+) PRE COST CALC -------------------------------------------------------
    if message.content.lower().startswith('add pre cost'):
        try:
            pcc_id = message.content.split(' ')[3]
            pcc_year = message.content.split(' ')[4]
        except IndexError:
            await message.channel.send('Η ΣΥΝΤΑΞΗ ΤΗΣ ΕΝΤΟΛΗΣ ΕΙΝΑΙ: {add pre cost + __code__ + __year__}')
            return
        pre_cost_calc.run(pcc_id, pcc_year)
        response = f"ΠΡΟΚΟΣΤΟΛΟΓΗΣΗ [{pcc_id}]: COMPLETE"
        await message.channel.send(response)

    # (-) (+) BAZAAR -------------------------------------------------------
    if message.content.lower().startswith('add bazaar'):
        delete_chat.run(5)
        bazaar.run()
        response = 'ΚΑΤΑΧΩΡΗΣΗ ΤΙΜΟΛΟΓΙΩΝ BAZAAR: COMPLETE'
        await message.channel.send(response)

    if message.content.lower().startswith('history'):
        price_history.run()
        await message.channel.send('ΔΗΜΙΟΥΡΓΙΑ ΙΣΤΟΡΙΚΟΥ ΤΙΜΩΝ: COMPLETE')


client.run(TOKEN)
