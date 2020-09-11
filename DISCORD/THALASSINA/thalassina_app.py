#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from Private import sql_connect
from DISCORD.THALASSINA import sql, excel, slack, plot


def run():
    file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/Θαλασσινά.xlsx'
    # -------------Pandas GET Answer ------------
    answer = pd.read_sql_query(sql.query_01(), sql_connect.connect())
    answer_2 = pd.read_sql_query(sql.query_02(), sql_connect.connect())
    answer_3 = pd.read_sql_query(sql.query_03(), sql_connect.connect())
    pl = answer_3.values.min()

    # ------------- PLOT ------------
    plot.figure(answer_2, answer)

    # ------------- EXCEL ------------
    excel.export(file_path, answer, answer_2, pl)

    # ------------- SLACK ------------
    slack.send(file_path)
