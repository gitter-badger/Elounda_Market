#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def get_product_cost(barcode):
    return f"""
           SELECT 
           ROUND(ESFIItemEntry_ESFIItemPeriodics.NetValue /
           isnull(ESFIItemEntry_ESFIItemPeriodics.Quantity, 1) ,2)                                     AS 'ΚΑΘΑΡΗ ΤΙΜΗ',
           FK_ESFIItemEntry_ESFIItem.Description                                                       AS 'ΠΕΡΙΓΡΑΦΗ',
           ESFIItemEntry_ESFIItemPeriodics.RegistrationDate                                            AS 'ΗΜΕΡΟΜΗΝΙΑ',
           DATEPART(yyyy,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)                             AS 'YEAR',
           FK_ESFIItemEntry_ESFIItem.BarCode                                                           AS 'BarCode'


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
    WHERE  FK_ESFIItemEntry_ESFIItem.BarCode = '{barcode}'
      AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤ%')
      AND (ESFIItemEntry_ESFIItemPeriodics.NetValue > 0) 
"""


def get_codes():
    return f"""
    SELECT FK_ESFIItemEntry_ESFIItem.BarCode, 
    DocumentCode
    FROM ESFIItemEntry_ESFIItemPeriodics

    LEFT JOIN ESFIItem AS FK_ESFIItemEntry_ESFIItem
                       ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = FK_ESFIItemEntry_ESFIItem.GID 
    LEFT JOIN ESFIDocumentTrade AS FK_ESFIItemEntry_ESFIDocumentTrade
                       ON ESFIItemEntry_ESFIItemPeriodics.fDocumentGID = FK_ESFIItemEntry_ESFIDocumentTrade.GID
    WHERE fTransitionStepCode = 'ΑΠΟΔΟΣΗ'
    """
