#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def get_product_cost(code):
    database_query = f"""
           SELECT TOP 1 
           ESFIItemEntry_ESFIItemPeriodics.RegistrationDate                                                     AS 'ΗΜΕΡΟΜΗΝΙΑ',
           ESFIItemEntry_ESFIItemPeriodics.DocumentCode                                                         AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
           FK_ESFIDocumentTrade_ESFITradeAccount.Name                                                           AS 'ΠΡΟΜΗΘΕΥΤΗΣ',
           FK_ESFIItemEntry_ESFIItem.BarCode                                                                    AS 'BARCODE',
           ESFIItemEntry_ESFIItemPeriodics.Quantity                                                             AS 'ΠΟΣΟΤΗΤΑ',
           FK_ESFIItemEntry_ESFIItem.Description                                                                AS 'ΠΕΡΙΓΡΑΦΗ',
           ESFIItemEntry_ESFIItemPeriodics.NetValue /
           isnull(ESFIItemEntry_ESFIItemPeriodics.Quantity, 1)                                                  AS 'ΚΑΘΑΡΗ ΤΙΜΗ',
           FK_ESFIItemEntry_ESFIItem.RetailPrice                                                                AS 'ΛΙΑΝΙΚΗ',
           Case when ESFIItemEntry_ESFIItemPeriodics.NetValue  =0 then null
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
    WHERE  FK_ESFIItemEntry_ESFIItem.BarCode = '{code}'
      AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤ%')

order by 1 DESC
    """
    return database_query


def pda_results(id):
    output = f"""
    SELECT IMP_MobileDocumentLines.BarCode as 'BARCODE' 
    FROM IMP_MobileDocumentLines 
    LEFT JOIN IMP_MobileDocumentHeaders ON 
    IMP_MobileDocumentLines.fDocGID = IMP_MobileDocumentHeaders.GID
    WHERE IMP_MobileDocumentHeaders.Code = {id}
    AND IMP_MobileDocumentHeaders.OrderType like 'ΑΠ_ΜΟΒ'
    """
    return  output

