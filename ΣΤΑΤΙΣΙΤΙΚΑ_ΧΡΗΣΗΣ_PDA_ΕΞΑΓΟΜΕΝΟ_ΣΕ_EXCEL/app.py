#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from ΣΤΑΤΙΣΙΤΙΚΑ_ΧΡΗΣΗΣ_PDA_ΕΞΑΓΟΜΕΝΟ_ΣΕ_EXCEL import excel_export, sql_query
from Private import sql_connect, slack_app
import pandas as pd

# ---------------- FILE PATH ----------------
path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/sql.xlsx'

# ---------------- ANSWERS ----------------
answer_01 = pd.read_sql_query(sql_query.query_01, sql_connect.sql_cnx())
answer_02 = pd.read_sql_query(sql_query.query_02, sql_connect.sql_cnx())
answer_03 = pd.read_sql_query(sql_query.query_03, sql_connect.sql_cnx())
answer_04 = pd.read_sql_query(sql_query.query_04, sql_connect.sql_cnx())
answer_05 = pd.read_sql_query(sql_query.query_05, sql_connect.sql_cnx())
answer_06 = pd.read_sql_query(sql_query.query_06, sql_connect.sql_cnx())

# ---------------- EXCEL EXPORT ----------------
excel_export.export(path, answer_01, answer_02, answer_03, answer_04, answer_05, answer_06)

# ---------------- SLACK BOT ----------------
slack_app.post_message_to_slack("""
>ΣΤΑΤΙΣΤΙΚΑ_ΧΡΗΣΗΣ_PDA
`Ενημερώθηκε Το Αρχείο: sql.xlsx`
""")
