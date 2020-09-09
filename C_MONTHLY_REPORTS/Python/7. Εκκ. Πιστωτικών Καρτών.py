#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect, send_mail
import pandas as pd
from C_MONTHLY_REPORTS.EXCEL import epc_07_to_excel


output_file = 'Sales_Credit_Card.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Εκκ. Πιστωτικών Καρτών (Κομμάς Ιωάννης)', 'Εκκ. Πιστωτικών Καρτών (Λογιστήριο)',
              'Εκκ. Πιστωτικών Καρτών (Κατάστημα)']
program_title = 'Εκκ. Πιστωτικών Καρτών '

# -------------------------------- READ HTML FILE ---------------------------------------
with open("../HTML/7. Εκκ. Πιστωτικών Καρτών.html", 'r')as html_file:
    word = html_file.read()

# -------------------------------- READ SQL FILE ---------------------------------------
with open('../SQL/7. Εκκ. Πιστωτικών Καρτών', 'r') as sql_file:
    sql_querry = sql_file.read()

# -------------------------------- SQL ---------------------------------------
sql_answer = pd.read_sql_query(sql_querry, sql_connect.sql_cnx())

# -------------------------------- EXCEL ---------------------------------------
epc_07_to_excel.run(path_to_file, sql_answer)

# -------------------------------- MAIL ---------------------------------------
send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)
