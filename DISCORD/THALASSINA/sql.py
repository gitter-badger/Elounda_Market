#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def query_01():
    return  """
    SELECT
           IsNull(FK_ESFIItem_ESFIZItemCategory.Description,'')
            AS Category
            ,isnull(Sum(ESFIItemPeriodics.TurnOver), 0) AS TurnOver
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2012 then TurnOver end), 0) '2012'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2013 then TurnOver end), 0) '2013'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2014 then TurnOver end), 0) '2014'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2015 then TurnOver end), 0) '2015'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2016 then TurnOver end), 0) '2016'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2017 then TurnOver end), 0) '2017'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2018 then TurnOver end), 0) '2018'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2019 then TurnOver end), 0) '2019'
        ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2020 then TurnOver end), 0) '2020'


    FROM ESFIItemPeriodics AS ESFIItemPeriodics
         LEFT JOIN ESFIItem AS FK_ESFIItemPeriodics_ESFIItem
           ON ESFIItemPeriodics.fItemGID = FK_ESFIItemPeriodics_ESFIItem.GID
         LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
           ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
         LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
           ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
         LEFT JOIN ESFIZItemCategory AS FK_ESFIItem_ESFIZItemCategory
           ON FK_ESFIItemPeriodics_ESFIItem.fItemCategoryCode = FK_ESFIItem_ESFIZItemCategory.Code AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemCategory.fCompanyCode
         WHERE
               (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
           AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
           AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
           AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
           AND (FK_ESFIItemPeriodics_ESFIItem.fItemGroupCode = '00-08')



    GROUP BY
     -- FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate,

    IsNull(FK_ESFIItem_ESFIZItemCategory.Description,'')
    """


def query_02():
    return """
    SELECT

         Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) as 'YEAR'
        ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver

    FROM ESFIItemPeriodics AS ESFIItemPeriodics
         LEFT JOIN ESFIItem AS FK_ESFIItemPeriodics_ESFIItem
           ON ESFIItemPeriodics.fItemGID = FK_ESFIItemPeriodics_ESFIItem.GID
         LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
           ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
         LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
           ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
         LEFT JOIN ESFIZItemCategory AS FK_ESFIItem_ESFIZItemCategory
           ON FK_ESFIItemPeriodics_ESFIItem.fItemCategoryCode = FK_ESFIItem_ESFIZItemCategory.Code
           AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemCategory.fCompanyCode
         WHERE
               (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
           AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
           AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
           AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
           AND (FK_ESFIItemPeriodics_ESFIItem.fItemGroupCode = '00-08')



    GROUP BY
      Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)

    """


def query_03():
    return """
    select 
    count(distinct(ESFIItem.fItemCategoryCode)) as count from ESFIItem
    where ESFIItem.fItemGroupCode = '00-08'
    """
