#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def private_database_query(name):
    return f"""
SELECT 
       ESFIItemEntry_ESFIItemPeriodics.DocumentCode                                                         AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
       FK_ESFIItemEntry_ESFIItem.BarCode                                                                    AS 'BARCODE',
       FK_ESFIItemEntry_ESFIItem.Description                                                                AS 'ΠΕΡΙΓΡΑΦΗ',
       FK_ESFIItemEntry_ESFIItem.fItemSubcategoryCode                                                       AS 'BRAND',
       ESFIItemEntry_ESFIItemPeriodics.Quantity                                                             AS 'ΠΟΣΟΤΗΤΑ',
       ESFIItemEntry_ESFIItemPeriodics.NetValue /
       isnull(ESFIItemEntry_ESFIItemPeriodics.Quantity, 1)                                                  AS 'ΚΑΘΑΡΗ ΤΙΜΗ',
       FK_ESFIItemEntry_ESFIItem.RetailPrice                                                                AS 'ΤΙΜΗ ΛΙΑΝΙΚΗΣ',
       CASE when ESFIItemEntry_ESFIItemPeriodics.NetValue  =0 then null
       Else (FK_ESFIItemEntry_ESFIItem.RetailPrice / (1 + (FK_ESFIItem_ESGOZVATCategory.Normal / 100))) /
       isnull((ESFIItemEntry_ESFIItemPeriodics.NetValue / ESFIItemEntry_ESFIItemPeriodics.Quantity), 1) -
       1 END                                                                                                    AS 'ΚΕΡΔΟΦΟΡΙΑ'
       

FROM ESFIItemEntry_ESFIItemPeriodics AS ESFIItemEntry_ESFIItemPeriodics

         LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem
                   ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem.GID
         LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItem
                   ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItem.GID
         LEFT JOIN ESFIDocumentTrade AS FK_ESFIItemEntry_ESFIDocumentTrade
                   ON ESFIItemEntry_ESFIItemPeriodics.fDocumentGID = FK_ESFIItemEntry_ESFIDocumentTrade.GID
         INNER JOIN ESFITradeAccount AS FK_ESFIDocumentTrade_ESFITradeAccount
                    ON FK_ESFIItemEntry_ESFIDocumentTrade.fTradeAccountGID = FK_ESFIDocumentTrade_ESFITradeAccount.GID
         LEFT JOIN ESGOZVATCategory AS FK_ESFIItem_ESGOZVATCategory
                   ON FK_ESFIItemEntry_ESFIItemPeriodics_ESFIItem.fVATCategoryCode = FK_ESFIItem_ESGOZVATCategory.Code
         LEFT JOIN ESFIZTransitionStep AS FK_ESFIDocumentTrade_ESFIZTransitionStep
                   ON FK_ESFIItemEntry_ESFIDocumentTrade.fTransitionStepCode =
                      FK_ESFIDocumentTrade_ESFIZTransitionStep.Code AND
                      FK_ESFIItemEntry_ESFIDocumentTrade.fCompanyCode =
                      FK_ESFIDocumentTrade_ESFIZTransitionStep.fCompanyCode
WHERE DATEPART(yyyy, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= DATEPART(yyyy, getdate())
  AND FK_ESFIDocumentTrade_ESFITradeAccount.Name = '{name}'
  AND FK_ESFIDocumentTrade_ESFIZTransitionStep.Description = 'ΣΕ ΠΡΟΕΤΟΙΜΑΣΙΑ'
  AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤΔ%')
         --  OR ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤΠ%')


ORDER BY 6
"""

