#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

#  ----- Read Me ----------------
# Step1: FILL  input_param = '' |
# Step2: RUN THE Program        |
# -------------------------------


import pandas as pd
from ΝΕΑ_ΠΑΡΑΓΓΕΛΙΑ import excel_export
from Private import slack_app, send_mail, sql_connect

# ----------------STATEMENTS HERE----------------------------
# 797 ok
input_param = '810'
output_file = "Order{}.xlsx".format(input_param)

# ----------------MAIL LIST----------------------------
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Νέα Παραγγελία: (Κομμάς)', 'Νέα Παραγγελία: (Λογιστήριο)', 'Νέα Παραγγελία: (Κατάστημα)']

# Open HTML File for the BODY MAIL
with open('body.html', 'r') as html_file:
    word = html_file.read()

# SQL QUERY ============================================================================================
sql_query = """
SELECT  BarCode, ItemDescription as 'Περιγραφή', quant as 'Ποσότητα'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {}
        and OrderType = 'ΠΠΡ'
        --and OrderType = 'ΔΕΑ'
""".format(input_param)

data_querry = """
SELECT  distinct OrderType as 'Type', IMP_MobileDocumentHeaders.Code as 'Code', ESFITradeAccount.Name as 'Name',
        IMP_MobileDocumentHeaders.PdaId as 'ID'
        FROM IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        left join ESFITradeAccount
        on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and IMP_MobileDocumentHeaders.Code = {}
        and OrderType = 'ΠΠΡ'
        --and OrderType = 'ΔΕΑ'
""".format(input_param)

extract_mail = """
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
        and IMP_MobileDocumentHeaders.Code = {}
        and OrderType = 'ΠΠΡ'
        --and OrderType = 'ΔΕΑ'
""".format(input_param)

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
answer_02 = pd.read_sql_query(data_querry, sql_connect.sql_cnx())
supplier = answer_02.Name[0]

# -------------ΒΡΕΣ ΤΟ MAIL ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ ----------------------------
person_mail = pd.read_sql_query(extract_mail, sql_connect.sql_cnx())
name = f'Νέα Παραγγελία: {katastima()}'
phone_number = person_mail.Telephone1[0]
for i in person_mail.EMailAddress:
    mail_lst.append(i)
    mail_names.append(name)
print(mail_lst)

# ----------------FILE PATH----------------------------
file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{k}/{s}/{f}'.format(s=supplier, f=output_file,
                                                                                     k=katastima())

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(file_path, answer_01, answer_02, katastima)

# -------------SEND E-MAIL----------------------------
send_mail.send_mail(mail_lst, mail_names, word, file_path, output_file)

# ----------------SLACK BOT----------------------------
slack_app.send_text(f"""
>ΚΑΤΑΧΩΡΗΘΗΚΕ Η ΠΑΡΑΓΓΕΛΙΑ
`ΑΡΧΕΙΟ: {output_file}`
`ΠΡΟΜΗΘΕΥΤΗΣ: {supplier}`
`ΥΠΟΚΑΤΑΣΤΗΜΑ: {katastima()}`
`PDA ID: {answer_02.ID[0]}`
`E-MAIL: {person_mail.EMailAddress[0]}`
`Τηλ.: {phone_number}`
""", slack_app.channels[3])

slack_app.send_files(output_file,file_path,'xlsx', slack_app.channels[3])
