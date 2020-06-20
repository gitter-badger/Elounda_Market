#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
path ='/Users/kommas/Downloads/file.xlsx'
df= pd.read_excel(path)
with open('file.csv', 'w') as file:
    x = [str(df['barcode'].iloc[i]) for i in range(len(df))]
    print(x)
    file.write('\,'.join(x).strip('.0'))
