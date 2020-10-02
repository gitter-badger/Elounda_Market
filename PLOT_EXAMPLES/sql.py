#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


# -----------| SQL QUERY | All Years | All Months | TZIROS | SALES|----------------------------------
def query_01():
    return """
SELECT
    format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy') as 'YEAR',
    month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) as 'MONTH'
  ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver

 FROM ESFIItemPeriodics
     LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
       ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
       ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
     WHERE
        (FK_ESFIItemPeriodics_ESGOSites.Code = '1')
GROUP BY

       format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy'),
        month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)
order by
        format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy'),
        month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)
"""
