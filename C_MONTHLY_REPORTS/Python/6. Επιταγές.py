#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import send_mail

output_file = 'read.txt'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Επιταγές (Κομμάς Ιωάννης)', 'Επιταγές (Λογιστήριο)', 'Επιταγές (Κατάστημα)']
program_title = 'Επιταγές'
# -------------------------------- READ HTML FILE ---------------------------------------
with open("../HTML/6. Επιταγές.html", 'r')as html_file:
    word = html_file.read()

# -------------------------------- MAIL ---------------------------------------
send_mail.send_mail(mail_lst, mail_names, word, output_file, output_file)