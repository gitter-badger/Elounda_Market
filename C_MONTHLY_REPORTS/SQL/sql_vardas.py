
#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def get_vardas_sale(date, code = '01-002284'):
    return f"""
        SELECT
           ESFIItem.BarCode AS ΚΩΔΙΚΟΣ,
           ESFIItem.Description AS ΠΕΡΙΓΡΑΦΗ,
           IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_SalesQty,0) AS SalesQuantity,
           IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_TurnOver,0) AS Turnover


    FROM ESFIItem AS ESFIItem
         LEFT JOIN (
                    SELECT ESFIItemEntry_ESFIItemPeriodics.fItemGID AS fItemGID,
                           Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty) AS ESFIItemPeriodics_SalesQty,
                           Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver) AS ESFIItemPeriodics_TurnOver,
                           IsNull(FK_ESFIItemEntry_ESGOSites_Site.Code,'') + ' - ' +
                           IsNull(FK_ESFIItemEntry_ESGOSites_Site.Description,'') AS Site_Descr,
                           ESFIItemEntry_ESFIItemPeriodics.fSiteGID AS fSiteGID
                    FROM ESFIItemEntry_ESFIItemPeriodics AS ESFIItemEntry_ESFIItemPeriodics

                         LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
                           ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
                         LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
                           ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
                    WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate in {date}
                           AND ((ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
                           OR (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver <> 0))


                    GROUP BY ESFIItemEntry_ESFIItemPeriodics.fItemGID, IsNull(FK_ESFIItemEntry_ESGOSites_Site.Code,'') + ' - ' +
                    IsNull(FK_ESFIItemEntry_ESGOSites_Site.Description,''), ESFIItemEntry_ESFIItemPeriodics.fSiteGID) AS FK_ItemSales_ESFIItem
           ON ESFIItem.GID = FK_ItemSales_ESFIItem.fItemGID
         LEFT JOIN (
                    SELECT ESFIItemEntry_ESFIItemPeriodics.fItemGID AS fItemGID,
                           Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty) AS ESFIItemPeriodics_SalesQty
                    FROM ESFIItemEntry_ESFIItemPeriodics AS ESFIItemEntry_ESFIItemPeriodics

                         LEFT JOIN ESGOSites AS FK_ESFIItemEntry_ESGOSites_Site
                           ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = FK_ESFIItemEntry_ESGOSites_Site.GID
                         LEFT JOIN ESFISalesPerson AS FK_ESFIItemEntry_ESFISalesPerson
                           ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = FK_ESFIItemEntry_ESFISalesPerson.GID
                    WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate in {date}
                            
                           AND (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)


                    GROUP BY ESFIItemEntry_ESFIItemPeriodics.fItemGID) AS FK_ItemSalesTotal_ESFIItem
           ON ESFIItem.GID = FK_ItemSalesTotal_ESFIItem.fItemGID
    WHERE
           ESFIItem.ItemClass <> 2
           and ESFIItem.Code = '{code}'


        """


def pistotiko():
    database_query = f"""
    SELECT ESFIItemEntry_ESFIItemPeriodics.RegistrationDate                                                     AS 'REGISTRATION DATE',
           ESFIItemEntry_ESFIItemPeriodics.NetValue                                                             AS 'NET VALUE',
           ESFIItemEntry_ESFIItemPeriodics.Comment                                                              AS 'COMMENT'
           

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
    WHERE DATEPART(yyyy, ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) >= 2019
      AND FK_ESFIItemEntry_ESFIItem.Code = '01-002284'
      AND (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΠΕΚ%')

    """
    return database_query