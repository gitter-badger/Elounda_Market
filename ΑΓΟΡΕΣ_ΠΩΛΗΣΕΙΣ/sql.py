#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
def sales(brands =('Aphrodite', 'Aphrodite') , year=2019):
    return f"""
        SELECT
    IsNull(FK_ESFIItemPeriodics_ESFIItem.BarCode,'') AS BARCODE
    ,ISNULL(FK_ESFIItemPeriodics_ESFIItem.Description, '') AS DESCRIPTION
    ,Sum(ESFIItemPeriodics.TurnOver) AS 'ΤΖΙΡΟΣ'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 1  then TurnOver end), 0) AS 'ΤΖΙΡΟΣ EM'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 3  then TurnOver end), 0) AS 'ΤΖΙΡΟΣ L1'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 5  then TurnOver end), 0) AS 'ΤΖΙΡΟΣ L2'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 6  then TurnOver end), 0) AS 'ΤΖΙΡΟΣ L3'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 7  then TurnOver end), 0) AS 'ΤΖΙΡΟΣ L4'

    ,Sum(ESFIItemPeriodics.SalesQty) AS 'ΠΩΛΗΣΕΙΣ'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 1  then SalesQty end), 0) AS 'ΠΩΛΗΣΕΙΣ EM'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 3  then SalesQty end), 0) AS 'ΠΩΛΗΣΕΙΣ L1'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 5  then SalesQty end), 0) AS 'ΠΩΛΗΣΕΙΣ L2'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 6  then SalesQty end), 0) AS 'ΠΩΛΗΣΕΙΣ L3'
    ,isnull(sum(case when FK_ESFIItemPeriodics_ESGOSites.Code = 7  then SalesQty end), 0) AS 'ΠΩΛΗΣΕΙΣ L4'


    FROM ESFIItemPeriodics
     LEFT JOIN ESFIItem AS FK_ESFIItemPeriodics_ESFIItem
       ON ESFIItemPeriodics.fItemGID = FK_ESFIItemPeriodics_ESFIItem.GID
     LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
       ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
       ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
     LEFT JOIN ESFIZItemSubCategory AS FK_ESFIItem_ESFIZItemSubCategory
       ON FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode = FK_ESFIItem_ESFIZItemSubCategory.Code
       AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemSubCategory.fCompanyCode
     WHERE
           (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemSubcategoryCode in {brands}) -- Υποκατηγορία (είσοδος)
       AND Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = {year}
    and FK_ESFIItemPeriodics_ESFIItem.Inactive = 0 and TurnOver > 0

    GROUP BY
    IsNull(FK_ESFIItemPeriodics_ESFIItem.BarCode,''),
    IsNull(FK_ESFIItemPeriodics_ESFIItem.Description, '')
    """


def cost(brands, year):
    return f"""
           SELECT
           FK_ESFIItemEntry_ESFIItem.BarCode                                                                    AS 'BARCODE'
           ,Sum(ESFIItemEntry_ESFIItemPeriodics.NetValue) AS 'ΚΟΣΤΟΣ'
            ,isnull(sum(case when ESGOSites.Code = 1  then ESFIItemEntry_ESFIItemPeriodics.NetValue end), 0) AS 'ΚΟΣΤΟΣ ΕΜ'
            ,isnull(sum(case when ESGOSites.Code = 3  then ESFIItemEntry_ESFIItemPeriodics.NetValue end), 0) AS 'ΚΟΣΤΟΣ L1'
            ,isnull(sum(case when ESGOSites.Code = 5  then ESFIItemEntry_ESFIItemPeriodics.NetValue end), 0) AS 'ΚΟΣΤΟΣ L2'
            ,isnull(sum(case when ESGOSites.Code = 6  then ESFIItemEntry_ESFIItemPeriodics.NetValue end), 0) AS 'ΚΟΣΤΟΣ L3'
            ,isnull(sum(case when ESGOSites.Code = 7  then ESFIItemEntry_ESFIItemPeriodics.NetValue end), 0) AS 'ΚΟΣΤΟΣ L4'

            ,Sum(ESFIItemEntry_ESFIItemPeriodics.Quantity) AS 'ΑΓΟΡΕΣ'
            ,isnull(sum(case when ESGOSites.Code = 1  then ESFIItemEntry_ESFIItemPeriodics.Quantity end), 0) AS 'ΑΓΟΡΕΣ EM'
            ,isnull(sum(case when ESGOSites.Code = 3  then ESFIItemEntry_ESFIItemPeriodics.Quantity end), 0) AS 'ΑΓΟΡΕΣ L1'
            ,isnull(sum(case when ESGOSites.Code = 5  then ESFIItemEntry_ESFIItemPeriodics.Quantity end), 0) AS 'ΑΓΟΡΕΣ L2'
            ,isnull(sum(case when ESGOSites.Code = 6  then ESFIItemEntry_ESFIItemPeriodics.Quantity end), 0) AS 'ΑΓΟΡΕΣ L3'
            ,isnull(sum(case when ESGOSites.Code = 7  then ESFIItemEntry_ESFIItemPeriodics.Quantity end), 0) AS 'ΑΓΟΡΕΣ L4'

           
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
            left join esgosites on FK_ESFIItemEntry_ESFIDocumentTrade.fADSiteGID = ESGOSites.GID
    WHERE  
          (ESFIItemEntry_ESFIItemPeriodics.DocumentCode LIKE 'ΑΤ%')
      AND (ESFIItemEntry_ESFIItemPeriodics.NetValue > 0) 
    and FK_ESFIItemEntry_ESFIItem.fItemSubcategoryCode in {brands}
      AND DATEPART(yyyy,ESFIItemEntry_ESFIItemPeriodics.RegistrationDate) = {year}
        and FK_ESFIItemEntry_ESFIItem.Inactive = 0

GROUP BY FK_ESFIItemEntry_ESFIItem.BarCode, FK_ESFIItemEntry_ESFIItem.Description
    """
     