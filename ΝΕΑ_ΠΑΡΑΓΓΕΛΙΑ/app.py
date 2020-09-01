#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

#  ----- Read Me ----------------
# Step1: FILL  input_param = '' |
# Step2: RUN THE Program        |
# -------------------------------
import sys
import os
import pandas as pd
from ΝΕΑ_ΠΑΡΑΓΓΕΛΙΑ import excel_export
from Private import slack_app, send_mail, sql_connect

# ----------------STATEMENTS HERE----------------------------
#
input_param = '826'
output_file = "Order{}.xlsx".format(input_param)
type_of_forma = 'ΠΠΡ'

# ----------------MAIL LIST----------------------------
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Νέα Παραγγελία: (Κομμάς)', 'Νέα Παραγγελία: (Λογιστήριο)', 'Νέα Παραγγελία: (Κατάστημα)']

# Open HTML File for the BODY MAIL
with open('body.html', 'r') as html_file:
    word = html_file.read()

# SQL QUERY ============================================================================================
sql_query = f"""
SELECT  BarCode, ItemDescription as 'Περιγραφή', quant as 'Ποσότητα'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""

data_query = f"""
SELECT  distinct OrderType as 'Type', IMP_MobileDocumentHeaders.Code as 'Code', ESFITradeAccount.Name as 'Name',
        IMP_MobileDocumentHeaders.PdaId as 'ID'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""

extract_mail = f"""
SELECT  
        distinct FK_ESGOPerson_PersonCode1.EMailAddress AS EMailAddress,
        FK_ESGOPerson_ESGOSites.Telephone1 AS Telephone1
        FROM IMP_MobileDocumentLines
        
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        LEFT JOIN ESGOPerson AS FK_ESGOPerson_PersonCode1
       ON ESFITradeAccount.fPersonCodeGID = FK_ESGOPerson_PersonCode1.GID 
       INNER JOIN ESGOSites AS FK_ESGOPerson_ESGOSites
       ON FK_ESGOPerson_PersonCode1.fMainAddressGID = FK_ESGOPerson_ESGOSites.GID
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {input_param}
        and OrderType = '{type_of_forma}'
        --and OrderType = 'ΔΕΑ'
"""


def katastima():
    if answer_02.ID[0] in ['00', '01']:
        return 'ΚΕΝΤΡΙΚΑ ΕΔΡΑΣ (ΣΧΙΣΜΑ ΕΛΟΥΝΤΑΣ)'
    elif answer_02.ID[0] == '10':
        return 'ΛΑΤΟ 01 (ΑΚΤΗ ΙΩΣΗΦ ΚΟΥΝΔΟΥΡΟΥ 11)'
    elif answer_02.ID[0] == '20':
        return 'ΛΑΤΟ 02 (28ΗΣ ΟΚΤΩΒΡΙΟΥ 6)'
    elif answer_02.ID[0] == '30':
        return 'ΛΑΤΟ 03 (ΑΓ. ΙΩΑΝΝΗΣ 29)'


# -------------ANSWERS----------------------------
answer_01 = pd.read_sql_query(sql_query, sql_connect.sql_cnx())
print(answer_01, end='\n')
answer_02 = pd.read_sql_query(data_query, sql_connect.sql_cnx())
print(answer_02, end='\n')
supplier = answer_02.Name[0]

# -------------ΑΝΑΘΕΣΗ ΤΙΜΗΣ: ΤΟ ΥΠΟΚΑΤΑΣΤΗΜΑ ----------------------------
store = katastima()
name = f'Νέα Παραγγελία: {store}'

# -------------DATAFRAME ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ ΜΑΙΛ - ΤΗΛΕΦΩΝΟ ----------------------------
person = pd.read_sql_query(extract_mail, sql_connect.sql_cnx())

# -------------ΒΡΕΣ ΤΟ ΤΗΛΕΦΩΝΟ ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ ----------------------------
phone_number = person.Telephone1[0]

# -------------ΠΡΟΣΘΕΤΩ ΤΟ MAIL ΣΤΗΝ ΛΙΣΤΑ ΜΕ ΤΑ MAILS ----------------------------
for i in person.EMailAddress:
    mail_lst.append(i)
    mail_names.append(name)
print(mail_lst)

# ----------------FILE PATH----------------------------
file_path = f'/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{store}/{supplier}/{output_file}'

# ----------------DIRECTORY PATH ----------------------------
directory_path = f'/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{store}/{supplier}'

# -------------------- MAKE DIRECTORY IF DOES NOT EXISTS --------------------
try:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print('!NEW! file path created')
    else:
        print('file path EXISTS')
except OSError:
    print("!ERROR! Creation of the directory FAILED")
    sys.exit(1)

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(file_path, answer_01, answer_02, store)

# -------------SEND E-MAIL----------------------------
send_mail.send_mail(mail_lst, mail_names, word, file_path, output_file)

# ----------------SLACK BOT----------------------------
slack_app.send_text(f"""
>ΚΑΤΑΧΩΡΗΘΗΚΕ Η ΠΑΡΑΓΓΕΛΙΑ
`ΑΡΧΕΙΟ: {output_file}`
`ΠΡΟΜΗΘΕΥΤΗΣ: {supplier}`
`ΥΠΟΚΑΤΑΣΤΗΜΑ: {store}`
`PDA ID: {answer_02.ID[0]}`
`E-MAIL: {person.EMailAddress[0]}`
`Τηλ.: {phone_number}`
>
>Data Science Tools Used:
>:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow:
""", slack_app.channels[3])

slack_app.send_files(output_file, file_path, 'xlsx', slack_app.channels[3])
