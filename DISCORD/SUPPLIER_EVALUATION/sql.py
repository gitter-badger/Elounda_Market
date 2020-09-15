#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def run(name, year):
    return f"""
SELECT 
        ESGOSites.Description                                               AS 'ΥΠΟΚΑΤΑΣΤΗΜΑ',
       ESFIItemEntry_ESFIItemPeriodics.DocumentCode                         AS 'ΠΑΡΑΣΤΑΤΙΚA',
        count(FK_ESFIItemEntry_ESFIItem.BarCode)                            AS 'ΓΡΑΜΜΕΣ',
        sum(ESFIItemEntry_ESFIItemPeriodics.Quantity)                       AS 'ΠΟΣΟΤΗΤΑ',
        FK_ESFIItemEntry_ESFIDocumentTrade.PayableAmount                    AS 'ΧΡΕΩΣΗ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Monday' then 1 end, 0) 'ΔΕΥΤΕΡΑ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Tuesday' then 1 end, 0) 'ΤΡΙΤΗ', 
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Wednesday' then 1 end, 0) 'ΤΕΤΑΡΤΗ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Thursday' then 1 end, 0) 'ΠΕΜΠΤΗ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Friday' then 1 end, 0) 'ΠΑΡΑΣΚΕΥΗ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Saturday' then 1 end, 0) 'ΣΑΒΒΑΤΟ',
isnull( case when datename(dw, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = 'Sunday' then 1 end, 0) 'ΚΥΡΙΑΚΗ'


FROM ESFIItemEntry_ESFIItemPeriodics AS ESFIItemEntry_ESFIItemPeriodics

         LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem
                   ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem.GID
         LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItem
                   ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItem.GID
         LEFT JOIN ESFIDocumentTrade AS FK_ESFIItemEntry_ESFIDocumentTrade
                   ON ESFIItemEntry_ESFIItemPeriodics.fDocumentGID = FK_ESFIItemEntry_ESFIDocumentTrade.GID
        left join ESGOSites on esgosites.gid = FK_ESFIItemEntry_ESFIDocumentTrade.fADSiteGID
         INNER JOIN ESFITradeAccount AS FK_ESFIDocumentTrade_ESFITradeAccount
                    ON FK_ESFIItemEntry_ESFIDocumentTrade.fTradeAccountGID = FK_ESFIDocumentTrade_ESFITradeAccount.GID
         LEFT JOIN ESGOZVATCategory AS FK_ESFIItem_ESGOZVATCategory
                   ON FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem.fVATCategoryCode = FK_ESFIItem_ESGOZVATCategory.Code
         LEFT JOIN ESFIZTransitionStep AS FK_ESFIDocumentTrade_ESFIZTransitionStep
                   ON FK_ESFIItemEntry_ESFIDocumentTrade.fTransitionStepCode =
                      FK_ESFIDocumentTrade_ESFIZTransitionStep.Code AND
                      FK_ESFIItemEntry_ESFIDocumentTrade.fCompanyCode =
                      FK_ESFIDocumentTrade_ESFIZTransitionStep.fCompanyCode
WHERE
    DATEPART(yyyy, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
    AND FK_ESFIDocumentTrade_ESFITradeAccount.Name = '{name}'
    AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤΔ%')

group by ESGOSites.Description, ESFIItemEntry_ESFIItemPeriodics.DocumentCode,
ESFIItemEntry_ESFIItemPeriodics.RegistrationDate,
 FK_ESFIItemEntry_ESFIDocumentTrade.PayableAmount

"""

