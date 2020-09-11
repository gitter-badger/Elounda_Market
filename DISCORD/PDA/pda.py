#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from DISCORD.PDA import excel, plot, slack, sql
from Private import sql_connect
import pandas as pd


def run():
    # ---------------- FILE PATH ----------------
    path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/sql.xlsx'
    # ---------------- ANSWERS ----------------
    answer_01 = pd.read_sql_query(sql.query_01, sql_connect.connect())
    answer_02 = pd.read_sql_query(sql.query_02, sql_connect.connect())
    answer_03 = pd.read_sql_query(sql.query_03, sql_connect.connect())
    answer_04 = pd.read_sql_query(sql.query_04, sql_connect.connect())
    answer_05 = pd.read_sql_query(sql.query_05, sql_connect.connect())
    answer_06 = pd.read_sql_query(sql.query_06, sql_connect.connect())
    # ---------------- PLOT ----------------
    plot.app(answer_03, answer_04, answer_05)
    # ---------------- EXCEL EXPORT ----------------
    excel.export(path, answer_01, answer_02, answer_03, answer_04, answer_05, answer_06)
    # ---------------- SLACK BOT ----------------
    slack.app(path)



