#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def run():
    return """
    SELECT DATEPART(YYYY, ESDCreated)  AS 'ΕΤΟΣ',
       COUNT(*)                    AS 'ΝΕΑ ΕΙΔΗ'                 
FROM ESFIITEM
WHERE DATEPART(YYYY, ESDCreated) > 2012
GROUP BY DATEPART(YYYY, ESDCreated)
    """
