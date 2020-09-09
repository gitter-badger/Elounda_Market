#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import send_mail

output_file = 'read.txt'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['PDA List (Κομμάς Ιωάννης)', 'PDA List (Λογιστήριο)', 'PDA List (Κατάστημα)']
program_title = 'PDA List'

# -------------------------------- READ HTML FILE ---------------------------------------
with open("../HTML/5. PDA LIST.html", 'r')as html_file:
    word = html_file.read()

# -------------------------------- MAIL ---------------------------------------
send_mail.send_mail(mail_lst, mail_names, word, output_file, output_file)
