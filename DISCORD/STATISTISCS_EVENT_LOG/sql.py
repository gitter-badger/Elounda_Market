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

def detailed():
    return """
    SELECT  
    (case when ES00EventLog.UserID in ('DESPOINA', 'DESP', 'KOUTOULAKI', 'XNARAKI', 'PEPONI', 'TAMEIO1', 'TAMEIO2') then 'ELOUNDA' 
              when ES00EventLog.UserID = 'TZANAKIS' then 'LATO 03'
              when ES00EventLog.UserID = 'XERSONISOS' then 'LATO 04'
              when ES00EventLog.UserID in ('ACCOUNT','M.RAPANAKI','MANIADAK','MARINA' ) then 'ΛΟΓΙΣΤΗΡΙΟ'
              when ES00EventLog.UserID in ('JOHNKOMMAS', 'RADMIN', 'ADMIN', 'KOMMAS') then 'ΙΤ'
              when ES00EventLog.UserID in ('KELLY', 'MARIA') then 'LATO 01'
              when ES00EventLog.UserID in ('BEGLO', 'ELOUNDAMARKET@YAHOO.GR','KOUTOULAKIS', 'KYRIAKOS', 'LATO 02', 'LATO1' ) then 'WMS'
    end)  AS STORE,

     year(EDate) AS DATE, 
     count(*) AS COUNT
    from ES00EventLog
    where ID = 'NO_ITEM_CODE_FOUND'
    
    group by case when ES00EventLog.UserID in ('DESPOINA', 'DESP', 'KOUTOULAKI', 'XNARAKI', 'PEPONI', 'TAMEIO1', 'TAMEIO2') then 'ELOUNDA' 
              when ES00EventLog.UserID = 'TZANAKIS' then 'LATO 03'
              when ES00EventLog.UserID = 'XERSONISOS' then 'LATO 04'
              when ES00EventLog.UserID in ('ACCOUNT','M.RAPANAKI','MANIADAK','MARINA' ) then 'ΛΟΓΙΣΤΗΡΙΟ'
              when ES00EventLog.UserID in ('JOHNKOMMAS', 'RADMIN', 'ADMIN', 'KOMMAS') then 'ΙΤ'
              when ES00EventLog.UserID in ('KELLY', 'MARIA') then 'LATO 01'
              when ES00EventLog.UserID in ('BEGLO', 'ELOUNDAMARKET@YAHOO.GR','KOUTOULAKIS', 'KYRIAKOS', 'LATO 02', 'LATO1' ) then 'WMS'
    end, year(EDate)
    """




def test():
    return """
        SELECT  UserID, count(*)
        from ES00EventLog
        where ID = 'NO_ITEM_CODE_FOUND'
        group by UserID
        
        """