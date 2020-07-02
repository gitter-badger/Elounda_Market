#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


from Private import sql_connect, slack_app, send_mail
import pandas as pd

output_file = 'Pendings.xlsx'

path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'

mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']

mail_names = ['Εκκρεμότητες (Κομμάς Ιωάννης)', 'Εκκρεμότητες (Λογιστήριο)', 'Εκκρεμότητες (Κατάστημα)']

program_title = 'Εκκρεμότητες'

with open("HTML/10. Εκκρεμότητες.html", 'r')as html_file:
    word = html_file.read()

# Read the SQL Querry_1
with open('SQL/10. Εκκρεμότητες Bazaar', 'r') as sql_file:
    sql_querry_1 = sql_file.read()

# Read the SQL Querry_2
with open('SQL/10. Εκκρεμότητες ELOUNDA MARKET', 'r') as sql_file:
    sql_querry_2 = sql_file.read()

# Read the SQL Querry_3
with open('SQL/10. Εκκρεμότητες LATO', 'r') as sql_file:
    sql_querry_3 = sql_file.read()

# Assign the SQL Query Answer
sql_answer_1 = pd.read_sql_query(sql_querry_1, sql_connect.sql_cnx())
sql_answer_2 = pd.read_sql_query(sql_querry_2, sql_connect.sql_cnx())
sql_answer_3 = pd.read_sql_query(sql_querry_3, sql_connect.sql_cnx())

tabs = ['Bazaar', 'Elounda', 'Lato']
answers = [sql_answer_1, sql_answer_2, sql_answer_3]
# Εισαγωγή Δεομένων στο  EXCEL
with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format=' dd - mm - yyyy') as writer:
    for i, tab in enumerate(tabs):
        answers[i].to_excel(writer, sheet_name=tab, startcol=0, startrow=0, index=None)

        # Φτιάχνω το excel για να είναι ευαναγνωστο
        workbook = writer.book
        worksheet = writer.sheets[tab]
        # Formats
        number = workbook.add_format({'num_format': '€#,##0.00',
                                      'align': 'left',
                                      'bold': False,
                                      "font_name": "Avenir Next"})
        normal = workbook.add_format({
            'align': 'left',
            'bold': False,
            "font_name": "Avenir Next"})
        percent = workbook.add_format({'num_format': '%#,##0.00',
                                       'align': 'left',
                                       'bold': False,
                                       "font_name": "Avenir Next"})
        # Fix Columns
        worksheet.set_column('A:A', 20, normal)
        worksheet.set_column('B:B', 15, normal)
        worksheet.set_column('C:C', 50, number)
        worksheet.set_column('D:D', 50, number)
        worksheet.set_column('E:E', 20, number)
        worksheet.set_column('F:F', 30, number)
        worksheet.set_column('G:G', 20, number)

# ----------------SLACK BOT delete----------------------------
x = (slack_app.history(slack_app.channels_id[4]))

for i in range(len(x['messages'])):
    timer = (x['messages'][i]['ts'])
    slack_app.delete(slack_app.channels_id[4], timer)

# ----------------SLACK BOT import----------------------------
slack_app.send_text("""
> ΜΗΝΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
`Ολοκληρώθηκε η εξαγωγή εκκρεμοτήτων για έως σήμερα:`
""", slack_app.channels[4])

slack_app.send_files(output_file, path_to_file, 'xlsx', slack_app.channels[4])

send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)
