#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.STATISTICS_NEW_ITEMS_PER_USER import sql, slack, plot
import pandas as pd
from datetime import datetime as dt

def run():
    # DATAFRAME
    df = pd.read_sql(sql.run(), sql_connect.connect())
    df2 = pd.read_sql(sql.run2(), sql_connect.connect())
    #PLOT
    name1 = 'images/new_items_per_user.png'
    name2 = 'images/new_items_per_user_all.png'
    plot.run(df, name1, dt.now().year )
    plot.run(df2, name2, f'FROM: 2012 TO: {dt.now().year}')
    # SLACK
    slack.run()
