#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

#  ----- Read Me ----------------
# Step1: FILL  input_param = '' |
# Step2: RUN THE Program        |
# -------------------------------
import sys
import os
import pandas as pd
from DISCORD.ORDER import sql, excel, slack

from Private import  sql_connect


def run(input_param):
    # ----------------STATEMENTS HERE----------------------------
    output_file = "Order{}.xlsx".format(input_param)
    type_of_forma = 'ΠΠΡ'

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
    answer_01 = pd.read_sql_query(sql.sql_query(input_param, type_of_forma), sql_connect.sql_cnx())
    print(answer_01, end='\n')
    answer_02 = pd.read_sql_query(sql.data_query(input_param, type_of_forma), sql_connect.sql_cnx())
    print(answer_02, end='\n')
    supplier = answer_02.Name[0]

    # -------------ΑΝΑΘΕΣΗ ΤΙΜΗΣ: ΤΟ ΥΠΟΚΑΤΑΣΤΗΜΑ ----------------------------
    store = katastima()
    name = f'Νέα Παραγγελία: {store}'

    # -------------DATAFRAME ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ ΜΑΙΛ - ΤΗΛΕΦΩΝΟ ----------------------------
    person = pd.read_sql_query(sql.extract_mail(input_param, type_of_forma), sql_connect.sql_cnx())

    # -------------ΒΡΕΣ ΤΟ ΤΗΛΕΦΩΝΟ ΤΟΥ ΠΡΟΜΗΘΕΥΤΗ ----------------------------
    phone_number = person.Telephone1[0]

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
    excel.export(file_path, answer_01, answer_02, store)

    # ----------------SLACK BOT----------------------------
    slack.run(output_file, supplier, store, answer_02, person, phone_number, file_path)
