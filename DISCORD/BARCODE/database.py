#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def sql_query():
 return """
SELECT [BarCode], COUNT(*) AS COUNTS
FROM ESFIItem
WHERE Inactive = 0
GROUP BY BARCODE
HAVING COUNT(*) > 1 and len(BARCODE) > 4
"""