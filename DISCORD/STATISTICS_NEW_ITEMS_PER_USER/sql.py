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


def run2():
    return """
    SELECT 'IT DEPARTMENT'              AS 'USER',
            COUNT(*)                    AS 'ΝΕΑ ΕΙΔΗ'
    FROM ESFIITEM
    WHERE ESUCreated in ('ADMIN', 'RADMIN', 'JOHNKOMMAS', 'ESMASTER', 'KOMMAS')
UNION
    SELECT 'ELOUNDA MARKET'             AS 'USER',
             COUNT(*)                   AS 'ΝΕΑ ΕΙΔΗ'
    FROM ESFIITEM
    WHERE ESUCreated in ('KYRIAKOS','ELOUNDAMARKET@YAHOO.GR', 'DESPOINA', 'DESP', 'MARIA' )
UNION
    SELECT 'LATO'                       AS 'USER',
            COUNT(*)                    AS 'ΝΕΑ ΕΙΔΗ'
    FROM ESFIITEM
    WHERE ESUCreated IN ('BADALAKIS', 'LATO1', 'BEGLO', 'TZANAKIS', 'XERSONISOS', 'USER1', 'MICHAEL', 'KELLY', 'GIAPAP7')
UNION
    SELECT 'LOGISTIRIO'                 AS 'USER',
            COUNT(*)                    AS 'ΝΕΑ ΕΙΔΗ'
    FROM ESFIITEM
    WHERE ESUCreated IN ('MARINA', 'MANIADAK', 'M.RAPANAKI', 'KATHEKLAKH', 'IES335@HOTMAIL.COM', 'ACCOUNT' )
    """