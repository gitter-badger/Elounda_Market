#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import asyncio
import os
import discord
from DISCORD.STATISTISCS_EVENT_LOG import no_item_found
from DISCORD.STATISTISCS_NEW_ITEMS import new_items
from DISCORD.STATISTICS_NEW_ITEMS_PER_USER import new_item_per_user
from Private import discord_app
from DISCORD.DELETE import delete_slack_chat
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
from datetime import datetime as dt
TOKEN = discord_app.token()
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! {dt.now().strftime("%H:%M:%S")}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel) == 'business-bot':
        # (-) (+) DAILY -------------------------------------------------------
        if message.content.lower().startswith('refresh daily'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(1)
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
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(4)
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
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(3)
            response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΑΡΑΓΓΕΛΙΕΣ: COMPLETE'
            await message.channel.send(response)

        # (+) ORDERS -------------------------------------------------------
        if message.content.lower().startswith('add order'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
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
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(6)
            response = 'ΔΙΑΓΡΑΦΗ ΚΑΝΑΛΙ: ΠΡΟ ΚΟΣΤΟΛΟΓΗΣΗ: COMPLETE'
            await message.channel.send(response)

        # (+) PRE COST CALC -------------------------------------------------------
        if message.content.lower().startswith('add pre cost'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
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
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(5)
            bazaar.run()
            response = 'ΚΑΤΑΧΩΡΗΣΗ ΤΙΜΟΛΟΓΙΩΝ BAZAAR: COMPLETE'
            await message.channel.send(response)

        # (+) PRICE HISTORY PLOT -------------------------------------------------------
        if message.content.lower().startswith('history'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
            price_history.run()
            await message.channel.send('ΔΗΜΙΟΥΡΓΙΑ ΙΣΤΟΡΙΚΟΥ ΤΙΜΩΝ: COMPLETE')

        # (+) DELETE DISCORD -------------------------------------------------------
        if message.content.lower().startswith('rm -rf'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
            await message.channel.purge(limit=100)

        # (+) ΣΤΑΤΙΣΤΙΚΗ DISCORD -------------------------------------------------------
        if message.content.lower().startswith('stats'):
            response = ':green_apple: Starting '
            await message.channel.send(response)
            delete_slack_chat.run(7)
            no_item_found.run()
            await message.channel.send('STATISTICS: ΣΦΑΛΜΑ ΣΤΟ ΤΑΜΕΙΟ / ΕΤΟΣ: COMPLETE')
            new_items.run()
            await message.channel.send('STATISTICS: ΝΕΑ ΕΙΔΗ / ΕΤΟΣ: COMPLETE')
            new_item_per_user.run()
            await message.channel.send('STATISTICS: ΝΕΑ ΕΙΔΗ / ΧΡΗΣΤΗ: COMPLETE /END')


# ---------------------------------------------------------------------------------------------------------------------
        # TODO ADD DOCUMENTATION

        # (+) DOCUMENTATION -------------------------------------------------------
        if message.content.lower() == 'help':
            await message.channel.send(file=discord.File("images/bot.png"))
            await message.channel.send("""
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ :arrow_right:  help κενό COMMAND
            """)

        if message.content.lower() == 'help delete pre cost':
            await message.channel.send("""
                        :one: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__ DELETE PRE COST :question:""")
            await message.channel.send("""
            :white_check_mark: ΠΡΟΣΟΧΗ: ΌΛΕΣ Οι Εγγραφές που έχουν γίνει στην Εφαρμογή Slack
            Στο Κανάλι προ_κοστολόγηση θα ΔΙΑΓΡΑΦΟΥΝ """)
            await message.channel.send(""" 
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΑΡΑΚΑΛΩ ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΣΤΟ::link: johnkommas@hotmail.com
            """)

        # (+) (+) DOCUMENTATION -------------------------------------------------------
        if message.content.lower() == 'help add pre cost':
            await message.channel.send("""
            :one: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__ ADD PRE COST :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΘΑ ΕΚΤΥΠΩΘΕΙ ΜΗΝΥΜΑ ΛΑΘΟΥΣ:
            Η ΣΥΝΤΑΞΗ ΤΗΣ ΕΝΤΟΛΗΣ ΕΙΝΑΙ: {add pre cost + code + year}
            """)
            await message.channel.send(':two: __TI__ __ΕΙΝΑΙ__ __ΤΟ__ __CODE__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΤΟ CODE ΕΙΝΑΙ Ο ΜΟΝΑΔΙΚΟΣ ΚΩΔΙΚΟΣ ΠΟΥ ΕΧΕΙ ΔΗΜΙΟΥΡΓΗΘΕΙ ΚΑΤΑ ΤΗΝ ΔΗΜΙΟΥΡΓΙΑ
            ΕΝΟΣ ΠΑΡΑΣΤΑΤΙΚΟΥ ΜΕΣΑ ΑΠΟ ΤΗΝ ΕΦΑΡΜΟΓΗ D-NET. ΑΥΤΟΝ ΤΟΝ ΚΩΔΙΚΟ
            ΠΡΕΠΕΙ ΝΑ ΕΙΣΑΓΟΥΜΕ. Ο ΤΥΠΟΣ ΠΑΡΑΣΤΑΤΙΚΟΥ ΠΟΥ ΕΠΙΛΕΓΟΥΜΕ ΓΙΑ ΤΗΝ
            ΠΡΟ ΚΟΣΤΟΛΟΓΗΣΗ ΤΩΝ ΕΙΔΩΝ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΔΕΑ (ΔΕΛΤΙΟ ΕΠΙΣΤΡΟΦΗΣ ΑΓΟΡΩΝ).
            """)
            await message.channel.send(':three: __TI__ __ΕΙΝΑΙ__ __ΤΟ__ __YEAR__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΤΟ YEAR ΕΙΝΑΙ ΤΟ ΕΤΟΣ ΓΙΑ ΤΟ ΟΠΟΙΟ ΘΕΛΟΥΜΕ ΝΑ ΓΙΝΕΙ Η ΚΟΣΤΟΛΟΓΗΣΗ
            ΕΙΝΑΙ ΠΛΕΟΝ ΔΕΔΟΜΕΝΟ ΟΤΙ ΟΙ ΤΙΜΕΣ ΑΓΟΡΑΣ ΤΩΝ ΠΡΟΪΟΝΤΩΝ ΑΛΛΑΖΟΥΝ
            ΑΠΟ ΕΤΟΣ ΣΕ ΕΤΟΣ. ΠΟΛΛΕΣ ΦΟΡΕΣ ΟΤΑΝ ΕΠΙΣΤΡΕΦΟΥΜΕ ΕΝΑ ΕΙΔΟΣ ΘΕΛΟΥΜΕ
            ΝΑ ΠΙΣΤΩΘΟΥΜΕ ΜΕ ΤΗΝ ΤΙΜΗ ΠΟΥ ΤΟ ΕΙΧΑΜΕ ΑΓΟΡΑΣΕΙ ΕΤΣΙ, ΑΝ ΕΝΑ ΠΡΟΪΟΝ 
            ΠΟΥ ΕΠΙΣΤΡΕΦΟΥΜΕ ΣΗΜΕΡΑ ΤΟ ΕΙΧΑΜΕ ΑΓΟΡΑΣΕΙ ΠΡΙΝ ΑΠΟ 2 ΕΤΗ ΘΕΛΟΥΜΕ ΝΑ ΓΝΩΡΙΖΟΥΜΕ
            ΤΟ ΚΟΣΤΟΣ ΑΓΟΡΑΣ ΤΟΥ ΣΥΓΚΕΚΡΙΜΕΝΟΥ ΕΤΟΥΣ. ΑΥΤΟ ΤΟ ΕΤΟΣ ΠΡΕΠΕΙ ΝΑ ΕΙΣΑΓΟΥΜΕ.
            """)
            await message.channel.send("""
            :four: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__  {add pre cost + code + year} :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΓΙΑ ΤΟ ΠΑΡΑΣΤΑΤΙΚΟ ΠΟΥ ΘΕΛΟΥΜΕ ΝΑ ΚΑΝΟΥΜΕ ΠΡΟ ΚΟΣΤΟΛΟΓΗΣΗ
            ΘΑ ΔΗΜΙΟΥΡΓΗΘΕΙ ΕΝΑ ΑΡΧΕΙΟ EXCEL.
            """)
            await message.channel.send(':five: __TI__ __ΠΕΡΙΕΧΕΙ__ __ΤΟ__ __EXCEL__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΠΕΡΙΕΧΕΙ ΤΙΣ ΕΞΗΣ ΠΛΗΡΟΦΟΡΙΕΣ:
            :blue_circle: BARCODE
            :blue_circle: ΠΕΡΙΓΡΑΦΗ
            :blue_circle: ΠΟΣΟΤΗΤΑ
            :blue_circle: ΚΑΘΑΡΗ ΤΙΜΗ
            :blue_circle: ΗΜΕΡΟΜΗΝΙΑ (ΑΓΟΡΑΣ)
            :blue_circle: ΠΑΡΑΣΤΑΤΙΚΟ (ΑΝΑΦΟΡΑΣ)
            :blue_circle: ΠΡΟΜΗΘΕΥΤΗΣ
            :blue_circle: SUM
            """)
            await message.channel.send(':six: __ΑΝ__ __ΕΧΩ__ __ΣΚΑΝΑΡΕΙ__ __ΤΟ__ __ΕΙΔΟΣ__ __2__ __ΦΟΡΕΣ__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΓΙΝΕΤΕ ΣΥΜΠΤΥΞΗ ΑΥΤΟΜΑΤΑ ΚΑΙ ΟΙ ΠΟΣΟΤΗΤΕΣ ΑΘΡΟΙΖΟΝΤΑΙ
            ΕΤΣΙ Ο ΚΩΔΙΚΟΣ ΕΙΝΑΙ ΜΟΝΑΔΙΚΟΣ
            """)
            await message.channel.send("""
            :seven: __ΑΝ__ __ΕΧΩ__ __ΑΓΟΡΑΣΕΙ__ __ΤΟ__ __ΕΙΔΟΣ__ __ΑΠΟ__ __ΠΟΛΛΑΠΛΟΥΣ__ __ΠΡΟΜΗΘΕΥΤΕΣ__ :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΔΕΝ ΜΑΣ ΕΠΗΡΕΑΖΕΙ ΚΑΘΩΣ ΚΑΤΑ ΤΗΝ ΑΝΑΖΗΤΗΣΗ ΕΧΟΥΜΕ ΦΡΟΝΤΙΣΕΙ
            ΝΑ ΜΑΣ ΦΕΡΕΙ ΤΙΣ ΑΓΟΡΕΣ ΓΙΑ ΤΟΝ ΠΡΟΜΗΘΕΥΤΗ ΠΟΥ ΘΑ ΕΠΙΣΤΡΕΨΟΥΜΕ ΤΑ ΕΙΔΗ
            """)
            await message.channel.send(':eight: __ΑΝ__ __ΕΧΩ__ __ΠΑΡΕΙ__ __ΔΩΡΑ__ __ΣΤΟ__ __ΕΤΟΣ__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΔΕΝ ΜΑΣ ΕΠΗΡΕΑΖΕΙ ΚΑΘΩΣ ΤΑ ΔΩΡΑ ΕΞΑΙΡΟΥΝΤΑΙ ΑΠΟ ΤΗΝ ΑΝΑΖΗΤΗΣΗ
            """)
            await message.channel.send("""
            :nine: __ΑΝ__ __ΚΑΤΑ__ __ΤΗΝ__ __ΔΙΑΡΚΕΙΑ__ __ΤΟΥ__ __ΕΤΟΥΣ__ __ΠΟΥ__ __ΑΝΑΖΗΤΩ__ __ΕΧΩ__ __ΑΓΟΡΑΣΕΙ__ __ΠΟΛΛΕΣ__ __ΦΟΡΕΣ__ :question:""")
            await message.channel.send(""" 
            :white_check_mark: Η ΤΙΜΗ ΑΓΟΡΑΣ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΜΙΑ, ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ ΜΕΣΗ ΤΙΜΗ
            ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ Η ΧΑΜΗΛΟΤΕΡΗ, ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ Η ΥΨΗΛΟΤΕΡΗ, ΘΑ ΕΙΝΑΙ ΠΑΝΤΑ 
            Η ΤΕΛΕΥΤΑΙΑ ΤΙΜΗ ΑΓΟΡΑΣ ΓΙΑ ΤΟ ΕΤΟΣ ΠΟΥ ΜΑΣ ΕΝΔΙΑΦΕΡΕΙ
            """)
            await message.channel.send("""
            :one: :zero: __ΑΝ__ __ΓΙΑ__ __ΤΟ__ __ΕΤΟΣ__ __ΔΕΝ__ __ΥΠΑΡΧΕΙ__ __ΑΓΟΡΑ__ :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΣΕ ΑΥΤΗΝ ΤΗΝ ΠΕΡΙΠΤΩΣΗ ΘΑ ΨΑΞΕΙ ΝΑ ΒΡΕΙ ΑΓΟΡΑ ΑΠΟ ΠΡΟΗΓΟΥΜΕΝΑ ΕΤΗ
            """)
            await message.channel.send("""
            :one: :one: __ΑΝ__ __ΚΑΙ__ __ΠΑΛΙ__ __ΔΕΝ__ __ΒΡΕΘΕΙ__ __ΠΑΡΑΣΤΑΤΙΚΟ__ __ΑΓΟΡΑΣ__ :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΤΟΤΕ ΕΙΜΑΣΤΕ ΣΙΓΟΥΡΟΙ ΟΤΙ ΤΟ ΕΙΔΟΣ ΕΙΝΑΙ ΝΕΟΤΕΡΟ ΤΟΥ ΕΤΟΥΣ 
            ΠΟΥ ΑΝΑΖΗΤΟΥΜΕ ΚΑΙ ΘΑ ΨΑΞΕΙ ΝΑ ΒΡΕΙ ΤΗΝ ΤΕΛΕΥΤΑΙΑ (ΠΙΟ ΠΡΟΣΦΑΤΗ ΤΙΜΗ ΑΓΟΡΑΣ)
            """)
            await message.channel.send(':one: :two: __ΤΙ__ __ΠΡΕΠΕΙ__ __ΝΑ__ __ΚΑΝΩ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΑΠΟ ΤΗΝ ΛΙΣΤΑ PICKING LIST ΒΡΙΣΚΕΙΣ ΤΟΝ ΚΩΔΙΚΟ ΤΟΥ ΠΑΡΑΣΤΑΤΙΚΟΥ
            ΚΑΙ ΕΙΣΑΓΕΙΣ ΤΟ ΕΤΟΣ ΠΟΥ ΕΠΙΘΥΜΕΙΣ ΝΑ ΠΑΡΕΙΣ ΚΟΣΤΟΣ ΑΓΟΡΑΣ  
            ΜΕΤΑ ΤΡΕΧΕΙΣ ΤΟΝ ΚΩΔΙΚΑ {ADD PRE COST CODE YEAR} ΕΔΩ ΚΑΙ ΠΕΡΙΜΕΝΕΙΣ ΛΙΓΟ.
            """)
            await message.channel.send(':one: :three: __ΤΑ__ __ΑΠΟΤΕΛΕΣΜΑΤΑ__ __ΠΟΥ__ __ΕΜΦΑΝΙΖΟΝΤΑΙ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΘΑ ΤΑ ΒΡΕΙΣ ΣΤΗΝ ΕΦΑΡΜΟΓΗ SLACK ΣΤΟ ΚΑΝΑΛΙ #προ κοστολογηση 
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΑΡΑΚΑΛΩ ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΣΤΟ::link: johnkommas@hotmail.com
            """)

        # (+) (+) DOCUMENTATION -------------------------------------------------------
        if message.content.lower() == 'help add bazaar':
            await message.channel.send("""
            :one: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__ ADD BAZAAR :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΓΙΑ ΚΑΘΕ ΠΑΡΑΣΤΑΤΙΚΟ ΤΥΠΟΥ ΑΤΔ
            ΜΕ ΒΗΜΑ "ΣΕ ΠΡΟΕΤΟΙΜΑΣΙΑ" ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ BAZAAR
            ΘΑ ΔΗΜΙΟΥΡΓΗΣΩ ΕΝΑ EXCEL ΑΡΧΕΙΟ ΚΑΙ ΕΝΑ ΓΡΑΦΗΜΑ
            """)
            await message.channel.send(':two: __TI__ __ΠΕΡΙΕΧΕΙ__ __ΤΟ__ __EXCEL__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΠΕΡΙΕΧΕΙ ΤΙΣ ΕΞΗΣ ΠΛΗΡΟΦΟΡΙΕΣ:
            :blue_circle: BARCODE
            :blue_circle: ΠΕΡΙΓΡΑΦΗ
            :blue_circle: ΠΟΣΟΤΗΤΑ
            :blue_circle: ΚΑΘΑΡΗ ΤΙΜΗ
            :blue_circle: ΤΙΜΗ ΛΙΑΝΙΚΗΣ
            :blue_circle: ΚΕΡΔΟΦΟΡΙΑ
            :blue_circle: ΤΙΜΗ ΛΙΑΝΙΚΗΣ [BAZAAR]
            :blue_circle: ΤΙΜΗ ΛΙΑΝΙΚΗΣ [ΒΑΣΙΛΟΠΟΥΛΟΣ]
            :blue_circle: ΤΙΜΗ ΛΙΑΝΙΚΗΣ [CARE MARKET] 
            ΕΧΕΙ ΓΙΝΕΙ ΟΜΑΔΟΠΟΙΗΣΗ ΜΕ ΒΑΣΗ ΤΟ BRAND NAME ΤΩΝ ΕΙΔΩΝ
            ΕΧΕΙ ΓΙΝΕΙ ΔΕΥΤΕΡΗ ΟΜΑΔΟΠΟΙΗΣΗ ΜΕ ΒΑΣΗ ΤΗΝ ΠΕΡΙΓΡΑΦΗ
            """)
            await message.channel.send(':three: __TI__ __ΠΕΡΙΕΧΕΙ__ __ΤΟ__ __ΓΡΑΦΗΜΑ__ :question:')
            await message.channel.send(""" 
            :white_check_mark: ΤΟ ΓΡΑΦΗΜΑ ΣΥΓΚΡΙΝΕΙ ΤΙΣ ΤΙΜΕΣ ΜΑΣ ΣΕ ΣΧΕΣΗ ΜΕ ΤΙΣ ΤΙΜΕΣ ΤΟΥ [BAZAAR]:
            :blue_circle: ΣΤΟΝ ΑΞΟΝΑ Χ ΒΡΙΣΚΟΝΤΑΙ ΤΑ ΕΙΔΗ
            :blue_circle: ΣΤΟΝ ΑΞΟΝΑ Υ ΕΙΝΑΙ Η ΤΙΜΗ (ΑΓΟΡΑΣ - ΛΙΑΝΙΚΗΣ - ΑΝΤΑΓΩΝΙΣΤΗ)
            ΕΧΕΙ ΓΙΝΕΙ ΟΜΑΔΟΠΟΙΗΣΗ ΜΕ ΒΑΣΗ ΤΗΝ ΤΙΜΗ ΑΓΟΡΑΣ
            """)
            await message.channel.send(':four: __ΤΙ__ __ΠΡΕΠΕΙ__ __ΝΑ__ __ΚΑΝΩ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΑΦΟΥ ΒΡΗΚΕΣ ΤΟ ΤΙΜΟΛΟΓΙΟ ΤΟΥ BAZAAR ΠΟΥ ΣΕ ΕΝΔΙΑΦΕΡΕΙ
            ΑΛΛΑΞΕ ΤΟ ΒΗΜΑ ΤΟΥ ΣΕ "ΣΕ ΠΡΟΕΤΟΙΜΑΣΙΑ" ΚΑΙ ΑΠΟΘΗΚΕΥΣΕ
            ΜΕΤΑ ΤΡΕΧΕΙΣ ΤΟΝ ΚΩΔΙΚΑ {ADD BAZAAR} ΕΔΩ ΚΑΙ ΠΕΡΙΜΕΝΕΙΣ ΛΙΓΟ.  
            """)
            await message.channel.send(':five: __ΤΑ__ __ΑΠΟΤΕΛΕΣΜΑΤΑ__ __ΠΟΥ__ __ΕΜΦΑΝΙΖΟΝΤΑΙ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΘΑ ΤΑ ΒΡΕΙΣ ΣΤΗΝ ΕΦΑΡΜΟΓΗ SLACK ΣΤΟ ΚΑΝΑΛΙ #bazaar 
            """)
            await message.channel.send("""
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΑΡΑΚΑΛΩ ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΣΤΟ::link: johnkommas@hotmail.com
            """)

        # (+) (+) DOCUMENTATION -------------------------------------------------------
        if message.content.lower() == 'help history':
            await message.channel.send("""
            :one: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__ HISTORY :question:""")
            await message.channel.send(""" 
            :white_check_mark: ΓΙΑ ΚΑΘΕ ΠΑΡΑΣΤΑΤΙΚΟ ΤΥΠΟΥ ΑΤΔ ή ΑΤΠ
            ΜΕ ΒΗΜΑ "ΑΠΟΔΟΣΗ" ΘΑ ΔΗΜΙΟΥΡΓΗΣΩ ΕΝΑΝ ΦΑΚΕΛΟ
            ΜΕΤΑ ΣΕ ΚΑΘΕ ΦΑΚΕΛΟ ΚΑΙ ΓΙΑ ΚΑΘΕ ΚΩΔΙΚΟ ΠΟΥ ΥΠΑΡΧΕΙ ΣΤΟ ΤΙΜΟΛΟΓΙΟ
            ΘΑ ΔΗΜΙΟΥΡΓΗΣΩ ΤΑ ΓΡΑΦΗΜΑΤΑ
            """)
            await message.channel.send(':two: __TI__ __ΑΠΕΙΚΟΝΙΖΟΥΝ__ __ΤΑ__ __ΓΡΑΦΗΜΑΤΑ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΤΑ ΓΡΑΦΗΜΑΤΑ ΣΤΟΝ ΑΞΟΝΑ Χ ΕΙΝΑΙ Ο ΧΡΟΝΟΣ
            ΚΑΙ ΣΤΟΝ ΑΞΟΝΑ Υ ΕΙΝΑΙ Η ΤΙΜΗ ΑΓΟΡΑΣ
            ΕΤΣΙ ΑΠΕΙΚΟΝΙΖΕΤΑΙ Η ΤΙΜΗ ΤΟΥΣ ΣΤΟ ΠΕΡΑΣΜΑ ΤΟΥ ΧΡΟΝΟΥ 
            """)
            await message.channel.send(':three: __ΤΙ__ __ΠΡΕΠΕΙ__ __ΝΑ__ __ΚΑΝΩ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΑΦΟΥ ΒΡΗΚΕΣ ΤΟ ΤΙΜΟΛΟΓΙΟ ΠΟΥ ΣΕ ΕΝΔΙΑΦΕΡΕΙ
            ΑΛΛΑΞΕ ΤΟ ΒΗΜΑ ΤΟΥ ΣΕ "ΑΠΟΔΟΣΗ" ΚΑΙ ΑΠΟΘΗΚΕΥΣΕ
            ΜΕΤΑ ΤΡΕΧΕΙΣ ΤΟΝ ΚΩΔΙΚΑ {HISTORY} ΕΔΩ ΚΑΙ ΠΕΡΙΜΕΝΕΙΣ ΛΙΓΟ.  
            """)
            await message.channel.send(':four: __ΤΑ__ __ΑΠΟΤΕΛΕΣΜΑΤΑ__ __ΠΟΥ__ __ΕΜΦΑΝΙΖΟΝΤΑΙ__ :question:')
            await message.channel.send("""
            :white_check_mark: ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΘΑ ΤΑ ΒΡΕΙΣ ΣΤΗΝ ΠΑΡΑΚΑΤΩ ΔΙΑΔΡΟΜΗ:
            :open_file_folder: OneDrive/Supplier_Check/history/{ΚΩΔΙΚΟΣ ΤΙΜΟΛΟΓΙΟΥ}/{ΕΔΩ ΕΙΝΑΙ ΤΑ ΑΡΧΕΙΑ}
            :e_mail: ΜΠΟΡΕΙΣ ΝΑ ΖΗΤΗΣΕΙΣ ΝΑ ΣΟΥ ΤΑ ΣΤΕΙΛΟΥΜΕ ΜΕ E-MAIL 
            """)
            await message.channel.send("""
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΑΡΑΚΑΛΩ ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΣΤΟ::link: johnkommas@hotmail.com
            """)

        # (+) (+) DOCUMENTATION -------------------------------------------------------
        if message.content.lower() == 'help rm -rf':
            await message.channel.send("""
            :one: __ΤΙ__ __ΘΑ__ __ΓΙΝΕΙ__ __ΑΝ__ __ΠΛΗΚΤΡΟΛΟΓΗΣΩ__ RM -RF :question:""")
            await message.channel.send("""
            :white_check_mark: ΘΑ ΔΙΑΓΡΑΦΟΥΝ ΟΛΕΣ ΟΙ ΕΓΓΡΑΦΕΣ ΠΟΥ ΒΡΙΣΚΟΝΤΑΙ ΣΕ ΑΥΤΟ ΤΟ ΚΑΝΑΛΙ ΣΤΟ DISCORD 
            """)
            await message.channel.send("""
            :information_source: ΓΙΑ ΠΕΡΙΣΣΟΤΕΡΕΣ ΠΛΗΡΟΦΟΡΙΕΣ ΠΑΡΑΚΑΛΩ ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΣΤΟ::link: johnkommas@hotmail.com
            """)
# ---------------------------------------------------------------------------------------------------------------------

    elif str(message.channel) == 'general-chat':

        # (+) DELETE DISCORD MESSAGES -------------------------------------------------------
        if message.content.lower().startswith('sudo rm -rf'):
            await message.channel.purge(limit=100)
        if message.content.lower().startswith('help'):
            await message.channel.send('Απαγορευμένη Ενέργεια')
            await asyncio.sleep(3)
            await message.channel.send('Επικοινωνήστε με τον Διαχειριστή')

    elif str(message.channel) == 'welcome':
        # (+) DELETE DISCORD MESSAGES -------------------------------------------------------
        if message.content.lower().startswith('sudo rm -rf'):
            await message.channel.purge(limit=100)
        if message.content.lower().startswith('help'):
            await message.channel.send('Απαγορευμένη Ενέργεια')
            await asyncio.sleep(3)
            await message.channel.send('Επικοινωνήστε με τον Διαχειριστή')

client.run(TOKEN)
