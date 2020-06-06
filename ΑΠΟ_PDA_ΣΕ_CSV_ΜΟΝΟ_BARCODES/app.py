#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from Private import sql_connect, slack_app
# ----------------SQL SELECT----------------------------
def pda_results(id):
    output = f"""
    SELECT IMP_MobileDocumentLines.BarCode as 'BARCODE' 
    FROM IMP_MobileDocumentLines 
    LEFT JOIN IMP_MobileDocumentHeaders ON 
    IMP_MobileDocumentLines.fDocGID = IMP_MobileDocumentHeaders.GID
    WHERE IMP_MobileDocumentHeaders.Code = {id}
    AND IMP_MobileDocumentHeaders.OrderType like 'ΑΠ_ΜΟΒ'
    """
    return output

# ----------------STATEMENTS HERE----------------------------
# 3/6/2020 '1875' DONE
# 4/6/2020 '1877' DONE
id = '1877'

# ----------------DATAFRAME----------------------------
df = pd.read_sql_query(pda_results(id), sql_connect.sql_cnx())

# ----------------FILE WRITE INLINE WITH \,----------------------------
with open('file.csv', 'w') as file:
    x = [str(df['BARCODE'].iloc[i]) for i in range(len(df))]
    print(x)
    file.write('\,'.join(x))

# ----------------SLACK BOT----------------------------
slack_app.post_message_to_slack(f""" 
H Αλλαγή Φ.Π.Α. Ολοκληρώθηκε 
PDA Αρχείο: {id}
""")