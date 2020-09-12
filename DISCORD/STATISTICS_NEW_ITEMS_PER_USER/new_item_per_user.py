#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.STATISTICS_NEW_ITEMS_PER_USER import sql, slack, plot
import pandas as pd


def run():
    # DATAFRAME
    df = pd.read_sql(sql.run(), sql_connect.connect())
    #PLOT
    plot.run(df)
    # SLACK
    slack.run(df)
