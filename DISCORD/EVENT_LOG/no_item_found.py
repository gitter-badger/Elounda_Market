#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.EVENT_LOG import sql
import pandas as pd

df = pd.read_sql(sql.run(), sql_connect.connect())


