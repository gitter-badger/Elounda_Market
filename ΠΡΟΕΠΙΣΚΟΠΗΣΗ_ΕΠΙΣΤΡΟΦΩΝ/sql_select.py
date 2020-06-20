#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def sql_query(input_param,order_type):
    return """
    SELECT  BarCode, ItemDescription as 'Περιγραφή', quant as 'Ποσότητα'
            FROM IMP_MobileDocumentLines
            left join IMP_MobileDocumentHeaders
            on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
            left join ESFITradeAccount
            on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
            where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
            --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
            and IMP_MobileDocumentHeaders.Code = {}
           -- and OrderType = 'ΠΠΡ'
            and OrderType = '{}'
    """.format(input_param, order_type)

def data_querry(input_param, order_type):
    return  """
    SELECT  distinct OrderType as 'Type', IMP_MobileDocumentHeaders.Code as 'Code', ESFITradeAccount.Name as 'Name',
            IMP_MobileDocumentHeaders.PdaId as 'ID'
            FROM IMP_MobileDocumentLines
            left join IMP_MobileDocumentHeaders
            on IMP_MobileDocumentHeaders.GID = IMP_MobileDocumentLines.fDocGID
            left join ESFITradeAccount
            on ESFITradeAccount.gid = IMP_MobileDocumentHeaders.Supplier
            where DATEPART(yyyy,RealImportTime) = DATEPART(yyyy,getdate())
            --and DATEPART(mm,RealImportTime) = DATEPART(mm,getdate())
            and IMP_MobileDocumentHeaders.Code = {}
            --and OrderType = 'ΠΠΡ'
            and OrderType = '{}'
    """.format(input_param, order_type)

def get_product_cost(code):
    database_query = f"""
           SELECT TOP 1 
           ESFIItemEntry_ESFIItemPeriodics.NetValue /
           isnull(ESFIItemEntry_ESFIItemPeriodics.Quantity, 1)                                                  AS 'ΚΑΘΑΡΗ ΤΙΜΗ',
           ESFIItemEntry_ESFIItemPeriodics.RegistrationDate                                                     AS 'ΗΜΕΡΟΜΗΝΙΑ',
           ESFIItemEntry_ESFIItemPeriodics.DocumentCode                                                         AS 'ΠΑΡΑΣΤΑΤΙΚΟ',
           FK_ESFIDocumentTrade_ESFITradeAccount.Name                                                           AS 'ΠΡΟΜΗΘΕΥΤΗΣ',
           FK_ESFIItemEntry_ESFIItem.BarCode                                                                    AS 'BarCode'


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

order by 2 DESC
    """
    return database_query