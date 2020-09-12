#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


def run():
    return """
    SELECT 
    DATEPART(yyyy, EDATE)   AS 'YEAR',
    count(*)                AS 'ΚΑΤΑΜΕΤΡΗΣΗ'
    from ES00EventLog
    where ID = 'NO_ITEM_CODE_FOUND'
    GROUP BY DATEPART(yyyy, EDATE)
    """



def run_today():
    return """
        SELECT
        UserID                  AS 'ΧΡΗΣΤΗΣ',
        --DATEPART(yyyy, EDATE)   AS 'YEAR',  
        count(*)                AS 'ΔΕΝ ΒΡΕΘΗΚΕ ΤΟ ΕΙΔΟΣ'
        from ES00EventLog
        where ID = 'NO_ITEM_CODE_FOUND'
        
        AND DATEPART(yyyy, EDATE) = DATEPART(yyyy, getdate())
        GROUP BY  UserID
        """


def parastatika_per_user(user):
    return f"""
SELECT 
    DATEPART(yyyy, EDATE)   AS 'YEAR',
    count(*)                AS 'ΔΙΑΓΡΑΦΗ PARASTATIKOY'
    from ES00EventLog
    where ID = 'DOCUMENTS_CANCELDATAENTRY'
    and UserID = '{user}'
    GROUP BY DATEPART(yyyy, EDATE)
"""


# """
# select * from ES00EventLog where
# --convert(varchar(10), EDATE, 102) = convert(varchar(10), getdate(), 102)
# DATEPART(yyyy, EDATE) = DATEPART(yyyy, getdate())
# """