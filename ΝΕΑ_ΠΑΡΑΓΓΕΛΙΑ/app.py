#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

#  ----- Read Me ----------------
# Step1: FILL  input_param = '' |
# Step2: RUN THE Program        |
# -------------------------------


import pandas as pd
from ΝΕΑ_ΠΑΡΑΓΓΕΛΙΑ import excel_export
from Private import slack_app, send_mail, sql_connect

# ----------------STATEMENTS HERE----------------------------
# 796 ok
input_param = '796'
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

# ----------------FILE PATH----------------------------
file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{k}/{s}/{f}'.format(s=supplier, f=output_file,
                                                                                     k=katastima())

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(file_path, answer_01, answer_02, katastima)

# -------------SEND E-MAIL----------------------------
send_mail.send_mail(mail_lst, mail_names, word, file_path, output_file)

# ----------------SLACK BOT----------------------------
slack_app.post_message_to_slack(f"""
ΚΑΤΑΧΩΡΗΘΗΚΕ Η ΠΑΡΑΓΓΕΛΙΑ : {output_file}
ΠΡΟΜΗΘΕΥΤΗΣ: {supplier}
ΥΠΟΚΑΤΑΣΤΗΜΑ: {katastima()}
ΑΠΟΤΥΠΩΜΑ: {answer_02.ID[0]}
............................
""")
