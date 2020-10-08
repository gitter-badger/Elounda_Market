#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.STATISTISCS_EVENT_LOG import sql, slack, plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def run():
    # DATAFRAME
    df = pd.read_sql(sql.run(), sql_connect.connect())
    detailed_df = pd.read_sql(sql.detailed(), sql_connect.connect())
    # PLOT
    plot.run(df, detailed_df)
    # SLACK
    slack.run()



    plt.show()
