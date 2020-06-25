#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ.library import timokatalogos

# -------------------- STATEMENTS HERE --------------------
choose = timokatalogos.lista_2020[-1]
from_date = choose.start
to_date = choose.end

x = pd.date_range(from_date, to_date)
print(x)
