#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
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
