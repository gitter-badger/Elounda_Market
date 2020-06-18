#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import sql_connect, send_mail, slack_app
from A_DAILY_REPORTS.Libraries import double_barcode_excel_export
import pandas as pd


output_file = 'Double_Barcodes.xlsx'

path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'

mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']

mail_names = ['Διπλά Barcodes (Κομμάς Ιωάννης)', 'Διπλά Barcodes (Λογιστήριο)', 'Διπλά Barcodes (Κατάστημα)']

program_title = 'Διπλά Barcodes '

barcode_old_values = ('5200116140910', '5206586230687', '5213002921425', '5214000237334')


with open('../HTML/double_barcode_body.html', 'r')as html_file:
    word = html_file.read()

# Read the SQL Querry
with open('../SQL/double_barcode_query.sql', 'r') as sql_file:
    sql_query = sql_file.read()


# Assign the SQL Query Answer
sql_answer = pd.read_sql_query(sql_query, sql_connect.sql_cnx())

sql_answer['Υπάρχει στο Slack'] = sql_answer.BarCode.apply(lambda x: 'NAI' if x in barcode_old_values else 'OXI')

print('DATA EXPORT PREVIEW')
print()
print(sql_answer)
print()

# Εισαγωγή Δεομένων στο  EXCEL
double_barcode_excel_export.export(path_to_file, sql_answer)

# SEND E-MAIL
# send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)

slack_app.send_text(f"""
>ΕΛΕΓΧΟΣ ΓΙΑ ΔΙΠΛΑ BARCODES 
```{sql_answer}```
""", slack_app.channels[1])