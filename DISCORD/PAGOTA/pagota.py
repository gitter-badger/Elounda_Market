#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from DISCORD.PAGOTA import sql, excel, slack, plot
from Private import sql_connect



def run():
    file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/Παγωτά.xlsx'
    # -------------Pandas GET Answer ------------
    answer = pd.read_sql_query(sql.query_01(), sql_connect.connect())
    answer_2 = pd.read_sql_query(sql.query_02(), sql_connect.connect())
    answer_3 = pd.read_sql_query(sql.query_03(), sql_connect.connect())
    pl = answer_3.values.min()

    # ------------- PLOT ------------
    plot.run(answer, answer_2)

    # ------------- EXCEL ------------
    excel.run(file_path, answer, answer_2, pl)

    # ------------- SLACK ------------
    slack.run(file_path)
