#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.ORDER import sql
import pandas as pd


def run():
    def katastima(x):
        if x in ['00', '01']:
            return 'ΚΕΝΤΡΙΚΑ ΕΔΡΑΣ (ΣΧΙΣΜΑ ΕΛΟΥΝΤΑΣ)'
        elif x == '10':
            return 'ΛΑΤΟ 01 (ΑΚΤΗ ΙΩΣΗΦ ΚΟΥΝΔΟΥΡΟΥ 11)'
        elif x == '20':
            return 'ΛΑΤΟ 02 (28ΗΣ ΟΚΤΩΒΡΙΟΥ 6)'
        elif x == '30':
            return 'ΛΑΤΟ 03 (ΑΓ. ΙΩΑΝΝΗΣ 29)'


    answer_01 = pd.read_sql_query(sql.available_orders(), sql_connect.connect())
    answer_01['Store'] = answer_01['PdaId'].apply(katastima)
    if len(answer_01)==0:
        return 'ΔΕΝ ΥΠΑΡΧΟΥΝ ΕΓΓΡΑΦΕΣ (ΠΑΡΑΓΓΕΛΙΕΣ)'
    else:
        return f'{answer_01}'

