#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def get_products_in_the_period(from_date, to_date):
    return f"""
SELECT ESFIPricelist.Code                         as 'ΤΙΜΟΚΑΤΑΛΟΓΟΣ',
       ESFIPricelistItem.fItemPricingCategoryCode as 'ΚΑΤΗΓΟΡΙΑ',
       ESFIPricelistItem.ValidFromDate            as 'ΕΝΑΡΞΗ',
       ESFIPricelistItem.ValidToDate              as 'ΛΗΞΗ',
       ESFIItem.Description                       AS 'ΠΕΡΙΓΡΑΦΗ',
       ESFIItem.BarCode                           AS 'ΚΩΔΙΚΟΣ',
       ESFIItem.RetailPrice                       as 'ΤΙΜΗ ΛΙΑΝΙΚΗΣ',
       ESFIPricelistItem.Price                    AS 'ΝΕΑ ΤΙΜΗ',
       ESFIPricelistItem.PercentageOnBasePrice    AS 'ΠΟΣΟΣΤΟ',
       ESFIItem.fItemSubcategoryCode              AS 'BRAND'
from ESFIPricelistItem
         left join ESFIItem
                   on ESFIPricelistItem.fItemGID = ESFIItem.GID
         inner JOIN ESFIPricelist
                    on ESFIPricelistItem.fPricelistGID = ESFIPricelist.GID
where '{from_date}' = ValidFromDate 
and     '{to_date}' = ValidToDate 
order by 3,4,5
"""


def get_sales(from_date, to_date, barcode_list):
    return f"""
    SELECT
       IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_SalesQty,0) AS SalesQuantity,
       IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_TurnOver,0) AS Turnover,
       ESFIItem.BarCode AS ΚΩΔΙΚΟΣ


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
                WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate >= '{from_date}'
                        AND ESFIItemEntry_ESFIItemPeriodics.RegistrationDate <= '{to_date}'
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
                WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate >= '{from_date}'
                        AND ESFIItemEntry_ESFIItemPeriodics.RegistrationDate <= '{to_date}'
                       AND (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)


                GROUP BY ESFIItemEntry_ESFIItemPeriodics.fItemGID) AS FK_ItemSalesTotal_ESFIItem
       ON ESFIItem.GID = FK_ItemSalesTotal_ESFIItem.fItemGID
WHERE
       ESFIItem.ItemClass <> 2
       and ESFIItem.BarCode in {barcode_list}
        

    """


def get_sales_for_every_day(specific_date, barcode_list):
    return f"""
    SELECT
       IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_SalesQty,0) AS SalesQuantity,
       IsNull(FK_ItemSales_ESFIItem.ESFIItemPeriodics_TurnOver,0) AS Turnover,
       ESFIItem.BarCode AS ΚΩΔΙΚΟΣ


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
                WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate = '{specific_date}'
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
                WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate = '{specific_date}'
                       AND (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)


                GROUP BY ESFIItemEntry_ESFIItemPeriodics.fItemGID) AS FK_ItemSalesTotal_ESFIItem
       ON ESFIItem.GID = FK_ItemSalesTotal_ESFIItem.fItemGID
WHERE
       ESFIItem.ItemClass <> 2
       and ESFIItem.BarCode in {barcode_list}


    """

def get_ending_pricelist_products(to_date):
    return f"""
    SELECT ESFIPricelist.Code                         as 'ΤΙΜΟΚΑΤΑΛΟΓΟΣ',
           ESFIPricelistItem.fItemPricingCategoryCode as 'ΚΑΤΗΓΟΡΙΑ',
           ESFIPricelistItem.ValidFromDate            as 'ΕΝΑΡΞΗ',
           ESFIPricelistItem.ValidToDate              as 'ΛΗΞΗ',
           ESFIItem.Description                       AS 'ΠΕΡΙΓΡΑΦΗ',
           ESFIItem.BarCode                           AS 'ΚΩΔΙΚΟΣ',
           ESFIItem.RetailPrice                       as 'ΤΙΜΗ ΛΙΑΝΙΚΗΣ',
           ESFIPricelistItem.Price                    AS 'ΝΕΑ ΤΙΜΗ',
           ESFIPricelistItem.PercentageOnBasePrice    AS 'ΠΟΣΟΣΤΟ',
           ESFIItem.fItemSubcategoryCode              AS 'BRAND'
    from ESFIPricelistItem
             left join ESFIItem
                       on ESFIPricelistItem.fItemGID = ESFIItem.GID
             inner JOIN ESFIPricelist
                        on ESFIPricelistItem.fPricelistGID = ESFIPricelist.GID
    where 
         '{to_date}' = ValidToDate 
    order by 3,4,5
    """

def get_rich_details(dates, barcode_list):
    return f"""
    SELECT
                       Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty) AS QUANTITY,
                       Sum(ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver) AS TURNOVER,
                        format(RegistrationDate, 'dd/MM/yyyy') as 'DATE',
                        ESFIitem.BarCode AS 'BARCODE',
                        ESFIitem.fItemSubcategoryCode AS 'BRAND'


                      -- ,day(ESFIItemEntry_ESFIItemPeriodics.RegistrationDate)

                FROM ESFIItemEntry_ESFIItemPeriodics

                     LEFT JOIN ESGOSites
                       ON ESFIItemEntry_ESFIItemPeriodics.fSiteGID = ESGOSites.GID
                     LEFT JOIN ESFISalesPerson
                       ON ESFIItemEntry_ESFIItemPeriodics.fSalesPersonGID = ESFISalesPerson.GID
                     LEFT JOIN  ESFIitem
                        ON ESFIItemEntry_ESFIItemPeriodics.fItemGID = ESFIitem.GID

                WHERE ESFIItemEntry_ESFIItemPeriodics.RegistrationDate in {dates}
                       AND ESFIitem.BarCode in {barcode_list}
                        AND ((ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_SalesQty <> 0)
                       OR (ESFIItemEntry_ESFIItemPeriodics.ESFIItemPeriodics_TurnOver <> 0))


GROUP BY ESFIItemEntry_ESFIItemPeriodics.fItemGID,format(RegistrationDate, 'dd/MM/yyyy'),ESFIitem.BarCode,
                        ESFIitem.fItemSubcategoryCode,

                        ESFIItemEntry_ESFIItemPeriodics.fSiteGID
    """

