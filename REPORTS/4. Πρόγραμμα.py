#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import send_mail, slack_app

output_file = 'a.pdf'

program_title = 'Πρόγραμμα:'

path_to_file = f'/Users/kommas/Downloads/{output_file}'

mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr', 'aikaterinakism@yahoo.gr']

mail_names = [f'{program_title} (Κομμάς Ιωάννης)',
              f'{program_title} (Λογιστήριο)',
              f'{program_title} (Κατάστημα)',
              f'{program_title} (Λογιστήριο)']

with open("/Users/kommas/PycharmProjects/Elounda_Market/REPORTS/HTML/4. Πρόγραμμα.html", 'r')as html_file:
    word = html_file.read()

# ----------------SLACK BOT----------------------------
slack_app.send_text('Το μηνιαίο Πρόγραμμα των Υπαλλήλων είναι Έτοιμο', slack_app.channels[1])
slack_app.send_files('report', path_to_file, 'pdf', slack_app.channels[2])

# ----------------MAIL BOT----------------------------
send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)
