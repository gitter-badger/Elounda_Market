#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import os
import discord
from Private import discord_app
from DISCORD import delete_chat
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

    if message.content == '!00':
        delete_chat.run(1)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΕΝΗΜΕΡΩΣΕΙΣ: COMPLETE'
        await message.channel.send(response)

    if message.content == '!01':
        double_barcode_check.run()
        response = 'ΕΛΕΓΧΟΣ ΓΙΑ ΔΙΠΛΑ BARCODES: COMPLETE '
        await message.channel.send(response)

    if message.content == '!02':
        elounda.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: ELOUNDA MARKET '
        await message.channel.send(response)

    if message.content == '!03':
        internet.run()
        response = 'ΕΛΕΓΧΟΣ INTERNET: COMPLETE '
        await message.channel.send(response)

    if message.content == '!04':
        pda.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ ΧΡΗΣΗΣ PDA: COMPLETE '
        await message.channel.send(response)

    if message.content == '!05':
        thalassina_app.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: ΘΑΛΑΣΣΙΝΑ: COMPLETE'
        await message.channel.send(response)

    if message.content == '!06':
        keroulis.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: ΚΕΡΟΥΛΗΣ: COMPLETE'
        await message.channel.send(response)

    if message.content == '!07':
        manaviki.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: MΑΝΑΒΙΚΗ: COMPLETE'
        await message.channel.send(response)

    if message.content == '!08':
        pagota.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: ΠΑΓΩΤΑ: COMPLETE'
        await message.channel.send(response)

    if message.content == '!09':
        delta.run()
        response = 'ΣΤΑΤΙΣΤΙΚΑ: ΔΕΛΤΑ ΦΡ. ΓΑΛΑ: COMPLETE'
        await message.channel.send(response)

    if message.content == '$00':
        delete_chat.run(4)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΕΚΚΡΕΜΟΤΗΤΕΣ: DONE'
        await message.channel.send(response)

    if message.content.split(' ')[0] == '+01':
        new_order.run(message.content.split(' ')[1])
        response = 'ΚΑΤΑΧΩΡΗΣΗ ΠΑΡΑΓΓΕΛΙΑΣ: COMPLETE'
        await message.channel.send(response)

    if message.content == '+00':
        delete_chat.run(3)
        response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΑΡΑΓΓΕΛΙΕΣ: DONE'
        await message.channel.send(response)

    if message.content.lower() == 'help':
        response = """
        AVAILABLE BOT COMMANDS
            SLACK 
                ΕΝΗΜΕΡΩΣΕΙΣ
                    0. [command: !00]: (ΔΙΑΓΡΑΦΕΙ ΤΙΣ ΕΝΗΜΕΡΩΣΕΙΣ)
                    1. [command: !01]: (ΕΛΕΓΧΟΣ ΓΙΑ ΔΙΠΛΑ BARCODES)
                    2. [command: !02]: (ΣΤΑΤΙΣΤΙΚΑ: ELOUNDA MARKET)
                    3. [command: !03]: (ΕΛΕΓΧΟΣ INTERNET)
                    4. [command: !04]: (ΣΤΑΤΙΣΤΙΚΑ: ΧΡΗΣΗ PDA)
                    5. [command: !05]: (ΣΤΑΤΙΣΤΙΚΑ: ΘΑΛΑΣΣΙΝΑ)
                    6. [command: !06]: (ΣΤΑΤΙΣΤΙΚΑ: ΚΕΡΟΥΛΗΣ)
                    7. [command: !07]: (ΣΤΑΤΙΣΤΙΚΑ: ΜΑΝΑΒΙΚΗ)
                    8. [command: !08]: (ΣΤΑΤΙΣΤΙΚΑ: ΠΑΓΩΤΑ)
                    9. [command: !09]: (ΣΤΑΤΙΣΤΙΚΑ: ΔΕΛΤΑ ΦΡ. ΓΑΛΑ)
                ΕΚΚΡΕΜΟΤΗΤΕΣ
                    0. [command: $00]: (ΔΙΑΓΡΑΦΕΙ ΤΙΣ ΕΚΚΡΕΜΟΤΗΤΕΣ)
                    1. [command: $01]: (ΕΚΚΡΕΜΟΤΗΤΕΣ ΤΙΜΟΛΟΓΗΣΗΣ)
                    2. [command: $02]: (ΒΑΡΔΑΣ ΠΙΣΤΩΤΙΚΟ ΥΠΟΛΟΙΠΟ)
                ΠΡΟΣΦΟΡΕΣ
                    0. [command: @00]: (ΑΝΑΝΕΩΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ)
                ΠΑΡΑΓΓΕΛΙΕΣ
                    0. [command: +00]: (ΔΙΑΓΡΑΦΕΙ ΤΙΣ ΠΑΡΑΓΓΕΛΙΕΣ)
                    1. [command: +01 + {ΑΡΙΘΜΟΣ}]: (ΚΑΤΑΧΩΡΗΣΗ ΠΑΡΑΓΓΕΛΙΑΣ)

        """
        await message.channel.send(response)


client.run(TOKEN)
