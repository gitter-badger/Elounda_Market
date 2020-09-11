#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from DISCORD.PENDING import slack, sql, excel
from Private import sql_connect
import pandas as pd


def run():
    output_file = 'Pendings.xlsx'
    path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
    # Assign the SQL Query Answer
    sql_answer_1 = pd.read_sql_query(sql.query_01(), sql_connect.connect())
    sql_answer_2 = pd.read_sql_query(sql.query_02(), sql_connect.connect())
    sql_answer_3 = pd.read_sql_query(sql.query_03(), sql_connect.connect())
    tabs = ['Bazaar', 'Elounda', 'Lato']
    answers = [sql_answer_1, sql_answer_2, sql_answer_3]
    # Εισαγωγή Δεομένων στο  EXCEL
    excel.run(path_to_file, tabs, answers)
    # ---------------- SLACK ----------------------------
    slack.run(output_file, path_to_file)

