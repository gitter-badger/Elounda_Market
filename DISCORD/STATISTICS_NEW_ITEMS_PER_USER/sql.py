#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def run():
    return """
    SELECT ESUCreated                  AS 'USER',
       COUNT(*)                    AS 'ΝΕΑ ΕΙΔΗ'
FROM ESFIITEM
WHERE DATEPART(YYYY, ESDCreated) = datepart(yyyy, getdate())
GROUP BY ESUCreated
order by 2
    """