#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def query_01():
    return """
    SELECT ESFIDocumentTrade.ADRegistrationDate                                                                   AS 'Ημερομηνία Έκδοσης',
       ESFIDocumentTrade.ADCode                                                                               AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
       FK_ESFIDocumentTrade_ESFITradeAccount.Name                                                             AS ΕΠΩΝΥΜΙΑ,
       ESFIDocumentTrade.ADReasoning                                                                          AS 'ΚΑΤΑΣΚΕΥΑΣΤΗΣ / ΣΧΟΛΙΑ',
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Code + ' - ' +
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Description                                                      AS 'ΚΑΤΑΣΤΗΜΑ',
       FK_ESFIDocumentTrade_ESFIDocumentType.Description                                                      AS 'ΤΎΠΟΣ ΠΑΡΑΣΤΑΤΚΟΥ',
       ESFIDocumentTrade.ADAlternativeCode                                                                    AS 'ΚΩΔΙΚΟΣ ΠΡΟΜΗΘΕΥΤΗ'

FROM ESFIDocumentTrade AS ESFIDocumentTrade
         INNER JOIN ESFITradeAccount AS FK_ESFIDocumentTrade_ESFITradeAccount
                    ON ESFIDocumentTrade.fTradeAccountGID = FK_ESFIDocumentTrade_ESFITradeAccount.GID
         LEFT JOIN ESGOSites AS FK_ESGOSites_ESFIDocumentTrade_ADSite
                   ON ESFIDocumentTrade.fADSiteGID = FK_ESGOSites_ESFIDocumentTrade_ADSite.GID
         LEFT JOIN ESFIDocumentType AS FK_ESFIDocumentTrade_ESFIDocumentType
                   ON ESFIDocumentTrade.fADDocumentTypeGID = FK_ESFIDocumentTrade_ESFIDocumentType.GID
         INNER JOIN (
    SELECT ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID AS fDocumentUpdateProfileGID
    FROM ESFIDocumentUpdateProfileLine AS ESFIDocumentUpdateProfileLine
             LEFT JOIN ESFIEntryType AS FK_ESFIDocumentUpdateProfileLine_ESFIEntryType
                       ON ESFIDocumentUpdateProfileLine.fEntryTypeGID =
                          FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID
             RIGHT JOIN ESFIEntryTypeOperation AS FK_ESFIEntryTypeOperation_ESFIEntryType
                        ON FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID =
                           FK_ESFIEntryTypeOperation_ESFIEntryType.fEntryTypeGID
    WHERE (ESFIDocumentUpdateProfileLine.SourceType = 1)
      AND (ESFIDocumentUpdateProfileLine.UpdateEntryTable = 'ESFIItemEntry')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationTable = 'ESFITradeAccountPeriodics')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationField = 'PendingInvoices')

    GROUP BY ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID) AS FK_DeltioParalabhs_ESFIDocumentTrade
                    ON ESFIDocumentTrade.fADDocumentUpdateProfileGID =
                       FK_DeltioParalabhs_ESFIDocumentTrade.fDocumentUpdateProfileGID
WHERE (FK_ESFIDocumentTrade_ESFIDocumentType.MenuEntry = 3)
  AND (ESFIDocumentTrade.ADCancelState = 0)
  AND DATEPART(yyyy, ESFIDocumentTrade.ADRegistrationDate) = DATEPART(yyyy, getdate())
  AND (ESFIDocumentTrade.ADTransitionAvailability = 1)
  AND (ESFIDocumentTrade.ADTransitionState in (0, 1))
  AND (FK_ESFIDocumentTrade_ESFITradeAccount.Name = 'Bazaar A.E.')

ORDER BY FK_ESFIDocumentTrade_ESFIDocumentType.Description, ESFIDocumentTrade.ADRegistrationDate,
         ESFIDocumentTrade.ADCode
    """


def query_02():
    return """
SELECT ESFIDocumentTrade.ADRegistrationDate                                                                   AS 'Ημερομηνία Έκδοσης',
       ESFIDocumentTrade.ADCode                                                                               AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
       FK_ESFIDocumentTrade_ESFITradeAccount.Name                                                             AS ΕΠΩΝΥΜΙΑ,
       ESFIDocumentTrade.ADReasoning                                                                          AS 'ΚΑΤΑΣΚΕΥΑΣΤΗΣ / ΣΧΟΛΙΑ',
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Code + ' - ' +
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Description                                                      AS 'ΚΑΤΑΣΤΗΜΑ',
       FK_ESFIDocumentTrade_ESFIDocumentType.Description                                                      AS 'ΤΎΠΟΣ ΠΑΡΑΣΤΑΤΚΟΥ',
       ESFIDocumentTrade.ADAlternativeCode                                                                    AS 'ΚΩΔΙΚΟΣ ΠΡΟΜΗΘΕΥΤΗ'

FROM ESFIDocumentTrade AS ESFIDocumentTrade
         INNER JOIN ESFITradeAccount AS FK_ESFIDocumentTrade_ESFITradeAccount
                    ON ESFIDocumentTrade.fTradeAccountGID = FK_ESFIDocumentTrade_ESFITradeAccount.GID
         LEFT JOIN ESGOSites AS FK_ESGOSites_ESFIDocumentTrade_ADSite
                   ON ESFIDocumentTrade.fADSiteGID = FK_ESGOSites_ESFIDocumentTrade_ADSite.GID
         LEFT JOIN ESFIDocumentType AS FK_ESFIDocumentTrade_ESFIDocumentType
                   ON ESFIDocumentTrade.fADDocumentTypeGID = FK_ESFIDocumentTrade_ESFIDocumentType.GID
         INNER JOIN (
    SELECT ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID AS fDocumentUpdateProfileGID
    FROM ESFIDocumentUpdateProfileLine AS ESFIDocumentUpdateProfileLine
             LEFT JOIN ESFIEntryType AS FK_ESFIDocumentUpdateProfileLine_ESFIEntryType
                       ON ESFIDocumentUpdateProfileLine.fEntryTypeGID =
                          FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID
             RIGHT JOIN ESFIEntryTypeOperation AS FK_ESFIEntryTypeOperation_ESFIEntryType
                        ON FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID =
                           FK_ESFIEntryTypeOperation_ESFIEntryType.fEntryTypeGID
    WHERE (ESFIDocumentUpdateProfileLine.SourceType = 1)
      AND (ESFIDocumentUpdateProfileLine.UpdateEntryTable = 'ESFIItemEntry')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationTable = 'ESFITradeAccountPeriodics')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationField = 'PendingInvoices')

    GROUP BY ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID) AS FK_DeltioParalabhs_ESFIDocumentTrade
                    ON ESFIDocumentTrade.fADDocumentUpdateProfileGID =
                       FK_DeltioParalabhs_ESFIDocumentTrade.fDocumentUpdateProfileGID
WHERE (FK_ESFIDocumentTrade_ESFIDocumentType.MenuEntry = 3)
  AND (ESFIDocumentTrade.ADCancelState = 0)
  AND DATEPART(yyyy, ESFIDocumentTrade.ADRegistrationDate) = DATEPART(yyyy, getdate())
  AND (ESFIDocumentTrade.ADTransitionAvailability = 1)
  AND (ESFIDocumentTrade.ADTransitionState in (0, 1))
  AND (FK_ESFIDocumentTrade_ESFITradeAccount.Name != 'Bazaar A.E.')
  AND FK_ESGOSites_ESFIDocumentTrade_ADSite.Code = 1

ORDER BY FK_ESFIDocumentTrade_ESFIDocumentType.Description, ESFIDocumentTrade.ADRegistrationDate,
         ESFIDocumentTrade.ADCode    
    """


def query_03():
    return """
SELECT ESFIDocumentTrade.ADRegistrationDate                                                                   AS 'Ημερομηνία Έκδοσης',
       ESFIDocumentTrade.ADCode                                                                               AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
       FK_ESFIDocumentTrade_ESFITradeAccount.Name                                                             AS ΕΠΩΝΥΜΙΑ,
       ESFIDocumentTrade.ADReasoning                                                                          AS 'ΚΑΤΑΣΚΕΥΑΣΤΗΣ / ΣΧΟΛΙΑ',
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Code + ' - ' +
       FK_ESGOSites_ESFIDocumentTrade_ADSite.Description                                                      AS 'ΚΑΤΑΣΤΗΜΑ',
       FK_ESFIDocumentTrade_ESFIDocumentType.Description                                                      AS 'ΤΎΠΟΣ ΠΑΡΑΣΤΑΤΚΟΥ',
       ESFIDocumentTrade.ADAlternativeCode                                                                    AS 'ΚΩΔΙΚΟΣ ΠΡΟΜΗΘΕΥΤΗ'

FROM ESFIDocumentTrade AS ESFIDocumentTrade
         INNER JOIN ESFITradeAccount AS FK_ESFIDocumentTrade_ESFITradeAccount
                    ON ESFIDocumentTrade.fTradeAccountGID = FK_ESFIDocumentTrade_ESFITradeAccount.GID
         LEFT JOIN ESGOSites AS FK_ESGOSites_ESFIDocumentTrade_ADSite
                   ON ESFIDocumentTrade.fADSiteGID = FK_ESGOSites_ESFIDocumentTrade_ADSite.GID
         LEFT JOIN ESFIDocumentType AS FK_ESFIDocumentTrade_ESFIDocumentType
                   ON ESFIDocumentTrade.fADDocumentTypeGID = FK_ESFIDocumentTrade_ESFIDocumentType.GID
         INNER JOIN (
    SELECT ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID AS fDocumentUpdateProfileGID
    FROM ESFIDocumentUpdateProfileLine AS ESFIDocumentUpdateProfileLine
             LEFT JOIN ESFIEntryType AS FK_ESFIDocumentUpdateProfileLine_ESFIEntryType
                       ON ESFIDocumentUpdateProfileLine.fEntryTypeGID =
                          FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID
             RIGHT JOIN ESFIEntryTypeOperation AS FK_ESFIEntryTypeOperation_ESFIEntryType
                        ON FK_ESFIDocumentUpdateProfileLine_ESFIEntryType.GID =
                           FK_ESFIEntryTypeOperation_ESFIEntryType.fEntryTypeGID
    WHERE (ESFIDocumentUpdateProfileLine.SourceType = 1)
      AND (ESFIDocumentUpdateProfileLine.UpdateEntryTable = 'ESFIItemEntry')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationTable = 'ESFITradeAccountPeriodics')
      AND (FK_ESFIEntryTypeOperation_ESFIEntryType.DestinationField = 'PendingInvoices')

    GROUP BY ESFIDocumentUpdateProfileLine.fDocumentUpdateProfileGID) AS FK_DeltioParalabhs_ESFIDocumentTrade
                    ON ESFIDocumentTrade.fADDocumentUpdateProfileGID =
                       FK_DeltioParalabhs_ESFIDocumentTrade.fDocumentUpdateProfileGID
WHERE (FK_ESFIDocumentTrade_ESFIDocumentType.MenuEntry = 3)
  AND (ESFIDocumentTrade.ADCancelState = 0)
  AND DATEPART(yyyy, ESFIDocumentTrade.ADRegistrationDate) = DATEPART(yyyy, getdate())
  AND (ESFIDocumentTrade.ADTransitionAvailability = 1)
  AND (ESFIDocumentTrade.ADTransitionState in (0, 1))
  AND (FK_ESFIDocumentTrade_ESFITradeAccount.Name != 'Bazaar A.E.')
  AND FK_ESGOSites_ESFIDocumentTrade_ADSite.Code != 1

ORDER BY FK_ESFIDocumentTrade_ESFIDocumentType.Description, ESFIDocumentTrade.ADRegistrationDate,
         ESFIDocumentTrade.ADCode    
    """