#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from DISCORD.DELTA import excel, sql, slack, plot
from Private import sql_connect


def run():
    file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/Φρέσκο Γάλα Δέλτα POS.xlsx'
    # -------------Pandas GET Answer ------------
    answer = pd.read_sql_query(sql.query_01(), sql_connect.sql_cnx())
    answer_2 = pd.read_sql_query(sql.query_02(), sql_connect.sql_cnx())
    # ------------- PLOT ------------
    plot.run(answer_2)
    pl = 12
    # ------------- EXCEL ------------
    excel.run(file_path, answer, answer_2, pl)
    # ------------- SLACK ------------
    slack.run(file_path)
