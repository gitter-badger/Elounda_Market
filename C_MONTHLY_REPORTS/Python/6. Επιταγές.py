#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import send_mail, sql_connect
from C_MONTHLY_REPORTS.EXCEL import epitages_to_excel
import pandas as pd

output_file = 'epitages.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Επιταγές (Κομμάς Ιωάννης)', 'Επιταγές (Λογιστήριο)', 'Επιταγές (Κατάστημα)']
program_title = 'Επιταγές'
# -------------------------------- READ HTML FILE ---------------------------------------
with open("../HTML/6. Επιταγές.html", 'r')as html_file:
    word = html_file.read()

with open("../SQL/epitages.sql", 'r')as sql_file:
    sql = sql_file.read()
# -------------------------------- DATA ---------------------------------------
data = pd.read_sql(sql, sql_connect.connect())

# -------------------------------- EXCEL ---------------------------------------
epitages_to_excel.run(path_to_file,data)
quit()

# -------------------------------- MAIL ---------------------------------------
send_mail.send_mail(mail_lst, mail_names, word, output_file, output_file)