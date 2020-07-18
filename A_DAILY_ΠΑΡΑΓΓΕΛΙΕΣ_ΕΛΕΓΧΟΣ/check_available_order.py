#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import sql_connect
import pandas as pd

# SQL QUERY ============================================================================================
sql_query = """
SELECT  
        Code,
        PdaId
        from IMP_MobileDocumentHeaders
        where DATEPART(yyyy,Date) = DATEPART(yyyy,getdate())
        and OrderType = 'ΠΠΡ'
        and CheckState is null -- καταχωρημένο όχι (στο PC)
        and Ιntegrated = 1 -- ολοκληρωμένο ναι (στο PDA)
        
"""


def katastima(x):
    if x in ['00', '01']:
        return 'ΚΕΝΤΡΙΚΑ ΕΔΡΑΣ (ΣΧΙΣΜΑ ΕΛΟΥΝΤΑΣ)'
    elif x == '10':
        return 'ΛΑΤΟ 01 (ΑΚΤΗ ΙΩΣΗΦ ΚΟΥΝΔΟΥΡΟΥ 11)'
    elif x == '20':
        return 'ΛΑΤΟ 02 (28ΗΣ ΟΚΤΩΒΡΙΟΥ 6)'
    elif x == '30':
        return 'ΛΑΤΟ 03 (ΑΓ. ΙΩΑΝΝΗΣ 29)'


answer_01 = pd.read_sql_query(sql_query, sql_connect.sql_cnx())
answer_01['Store'] = answer_01['PdaId'].apply(katastima)
if len(answer_01)==0:
    print('ΔΕΝ ΥΠΑΡΧΟΥΝ ΕΓΓΡΑΦΕΣ (ΠΑΡΑΓΓΕΛΙΕΣ)')
else:
    print('ΒΡΕΘΗΚΑΝ ΕΓΓΡΑΦΕΣ (ΠΑΡΑΓΓΕΛΙΕΣ)')
    print(answer_01)
