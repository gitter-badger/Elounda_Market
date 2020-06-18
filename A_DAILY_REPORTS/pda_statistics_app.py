#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from A_DAILY_REPORTS.SQL import pda_stats_sql_query
from A_DAILY_REPORTS.Libraries import pda_stats_excel_export
from Private import sql_connect, slack_app
import pandas as pd

# ---------------- FILE PATH ----------------
path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/sql.xlsx'

# ---------------- ANSWERS ----------------
answer_01 = pd.read_sql_query(pda_stats_sql_query.query_01, sql_connect.sql_cnx())
answer_02 = pd.read_sql_query(pda_stats_sql_query.query_02, sql_connect.sql_cnx())
answer_03 = pd.read_sql_query(pda_stats_sql_query.query_03, sql_connect.sql_cnx())
answer_04 = pd.read_sql_query(pda_stats_sql_query.query_04, sql_connect.sql_cnx())
answer_05 = pd.read_sql_query(pda_stats_sql_query.query_05, sql_connect.sql_cnx())
answer_06 = pd.read_sql_query(pda_stats_sql_query.query_06, sql_connect.sql_cnx())

# ---------------- EXCEL EXPORT ----------------
pda_stats_excel_export.export(path, answer_01, answer_02, answer_03, answer_04, answer_05, answer_06)

# ---------------- SLACK BOT ----------------
slack_app.send_text("""
>ΣΤΑΤΙΣΤΙΚΑ_ΧΡΗΣΗΣ_PDA
`Ενημερώθηκε Το Αρχείο: sql.xlsx`
""", slack_app.channels[1])
slack_app.send_files('sql.xlsx', path, 'xlsx', slack_app.channels[1])
