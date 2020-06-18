#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

# -----------FUNCTION SQL QUERY-------------------------------------------
query_01 = """
        SELECT  IMP_MobileDocumentHeaders.OrderType AS OrderType,
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        left join IMP_MobileDocumentHeaders
        on  IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and DATEPART(dd,RealImportTime) = DATEPART(dd,getdate())
        group by IMP_MobileDocumentHeaders.OrderType
        order by  2 desc"""

# Παραλαβές | Σήμερα | GROUP BY Ώρα -----------------------------------------
query_02 = """
        SELECT DATEPART(hh,RealImportTime) as 'HOUR',
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        and DATEPART(dd,RealImportTime) = DATEPART(dd,getdate())
        group by DATEPART(hh,RealImportTime)
        order by HOUR"""

# Παραλαβές |  | GROUP BY ΗΜΕΡΑ --------------------------------------------
query_03 = """
SELECT DATEPART(dd,RealImportTime) as 'DAY',
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
        group by DATEPART(dd,RealImportTime)
        order by DAY
"""
# Παραλαβές |  | GROUP BY ΜΗΝΑΣ --------------------------------------------
query_04 = """
SELECT DATEPART(mm,RealImportTime) as 'MONTH',
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
        group by DATEPART(mm,RealImportTime)
        order by MONTH
"""

# Παραλαβές |  | GROUP BY ΕΤΟΣ ----------------------------------------------
query_05 = """
SELECT DATEPART(yyyy,RealImportTime) as 'YEAR',
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        group by DATEPART(yyyy,RealImportTime)
        order by YEAR

"""
# Παραλαβές |  | GROUP BY ΩΡΑ  ------------------------------------------------
query_06 = """
        SELECT DATEPART(hh,RealImportTime) as 'HOUR',
        count(*) as 'Count "Γραμμές"',
        count(distinct(fDocGID)) as 'Count "Παραστατικά"'
        FROM ATSALIS.dbo.IMP_MobileDocumentLines
        group by DATEPART(hh,RealImportTime)
        order by HOUR
"""
