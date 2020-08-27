#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from B_WEEKLY_ΕΝΗΜΕΡΩΣΗ_ΕΙΣΑΓΩΓΗΣ_ΠΑΡΑΣΤΑΤΙΚΩΝ.Libraries import sql_import_report, scrap, excel_writer
from Private import send_mail, slack_app, sql_connect


# -------------------- Statements Here --------------------
output_file = 'Bazaar.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Τιμολόγιο Bazaar (Κομμάς)', 'Τιμολόγιο Bazaar (Λογιστήριο)', 'Τιμολόγιο Bazaar (Κατάστημα)']
main_name = 'Bazaar A.E.'


# -------------------- Open HTML File for the BODY MAIL --------------------
with open('HTML/2. Import || Bazaar.html', 'r') as html_file:
    word = html_file.read()


# -------------------- Assign the SQL Query Answer --------------------
sql_answer = pd.read_sql_query(sql_import_report.private_database_query(main_name), sql_connect.sql_cnx())


# -------------------- ASSIGN VALUES HERE MARKUP / QUARTILES --------------------
markup = round(sql_answer['ΚΕΡΔΟΦΟΡΙΑ']*100, 2)
quartiles = np.quantile(markup, [.25, .5, .75])
order_id = sql_answer['ΠΑΡΑΣΤΑΤΙΚΟ'].unique()
retail_price = sql_answer['ΤΙΜΗ ΛΙΑΝΙΚΗΣ']
retail_q = np.quantile(retail_price, [.25, .5, .75])

# -------------------- FIND BARCODES WHO ARE IN EVERY QUARTILE --------------------
codes_in_q1 = sql_answer[markup <= quartiles[0]]
codes_in_q2 = sql_answer[(markup > quartiles[0]) & (markup <= quartiles[1])]
codes_in_q3 = sql_answer[(markup > quartiles[1]) & (markup <= quartiles[2])]
codes_in_q4 = sql_answer[markup > quartiles[2]]


if input('Press 1 to Start:') != '1':
    quit()

# -------------------- Make the list to query for every barcode in bazaar web page --------------------
lista = sql_answer['BARCODE']
scrap.shops = [scrap.a, scrap.b, scrap.e]
out = scrap.calculate_prices(lista)


# -------------------- Assign the results --------------------
sql_answer['ΤΙΜΗ BAZAAR'] = out['BAZAAR']
sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'] = out['ΑΒ. Βασιλόπουλος']
sql_answer['TIMH Care Market'] = out['Care Market']

# -------------------- PLOT A HISTOGRAM WITH QUARTILE VALUES --------------------
# create your figure here
plt.figure(figsize=(15, 9))
# First Subplot
plt.subplot(2, 1, 1, xlabel='Markup (%100)', ylabel='Count', title=f'{order_id} [Histogram (Quartiles)]')
plt.hist(markup, bins=8)
plt.axvline(x=quartiles[0], label=f"Q1={quartiles[0]}", c ='#6400e4')
plt.axvline(x=quartiles[1], label=f"Q2={quartiles[1]}", c ='#fd4d3f')
plt.axvline(x=quartiles[2], label=f"Q3={quartiles[2]}", c ='#4fe0b0')
plt.grid(True, alpha=0.2)
plt.legend()
# Second Subplot
plt.subplot(2, 2, 4, xlabel='Product', ylabel='Retail Price', title='Retail Price [Scatter Plot]')
plt.scatter(range(len(sql_answer)), retail_price, marker='o', color='blue', label='ELOUNDA')
plt.scatter(range(len(sql_answer)), sql_answer['ΤΙΜΗ BAZAAR'], marker='o', color='red', label='BAZAAR')
# plt.scatter(range(len(sql_answer)), sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'], marker='o', color='green', label='ΒΑΣΙΛΟΠΟΥΛΟΣ')
# plt.scatter(range(len(sql_answer)), sql_answer['TIMH Care Market'], marker='o', color='black', label='Care Market')
plt.grid(True, alpha=0.2)
plt.legend()
# Next Subplot
plt.subplot(2, 2, 3, xlabel='BoxPlot', ylabel='Markup (%100)', title='Markup [Box Plot]')
plt.boxplot(markup)
plt.grid(True, alpha=0.2)
# Save Figure as Image and Plot
plt.savefig('views.png')
plt.show()

# -------------------- Εισαγωγή Δεομένων στο  EXCEL --------------------
excel_writer.export(path_to_file, sql_answer)


# ---------------- E-MAIL SEND --------------------
send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)

# ----------------SLACK BOT----------------------------
slack_output_text = f"""
> ΕΒΔΟΜΑΔΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
> ΚΑΤΑΧΩΡΗΘΗΚΑΝ ΤΑ ΤΙΜΟΛΟΓΙΑ: {order_id}
"""

slack_app.send_text(slack_output_text, slack_app.channels[5])

slack_app.send_files(output_file, path_to_file, 'xlsx', slack_app.channels[5])
slack_app.send_files('views.png', 'views.png', 'png', slack_app.channels[5])