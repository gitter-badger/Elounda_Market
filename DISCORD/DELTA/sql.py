#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

# -----------| SQL QUERY -------------
def query_01():
    return """
SELECT

           case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=1 then 'ΙΑΝΟΥΑΡΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=2 then 'ΦΕΒΡΟΥΑΡΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=3 then 'ΜΑΡΤΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=4 then 'ΑΠΡΙΛΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=5 then 'ΜΑΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=6 then 'ΙΟΥΝΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=7 then 'ΙΟΥΛΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=8 then 'ΑΥΓΟΥΣΤΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=9 then 'ΣΕΠΤΕΜΒΡΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=10 then 'ΟΚΤΩΒΡΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=11 then 'ΝΟΕΜΒΡΙΟΣ'
                when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)=12 then 'ΔΕΚΕΜΒΡΙΟΣ'
           end
    ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver
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
     LEFT JOIN ESFIZItemSubCategory AS FK_ESFIItem_ESFIZItemSubCategory
       ON FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode = FK_ESFIItem_ESFIZItemSubCategory.Code AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemSubCategory.fCompanyCode
     WHERE
           (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
       AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
       AND (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002885') 
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000239')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002886')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000241')





GROUP BY
 month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)

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
     LEFT JOIN dbo.ESFIZItemSubCategory AS FK_ESFIItem_ESFIZItemSubCategory
       ON FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode = FK_ESFIItem_ESFIZItemSubCategory.Code 
       AND FK_ESFIItemPeriodics_ESFIItem.fCompanyCode = FK_ESFIItem_ESFIZItemSubCategory.fCompanyCode
     WHERE
           (FK_ESFIItemPeriodics_ESFIItem.AssemblyType <> 1) --όχι τα σετ
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemType <> 6) -- όχι εγγυοδοσία
       AND (FK_ESFIItemPeriodics_ESFIItem.ItemClass = 1)  -- Κλάση Είδη Αποθήκης (1)
       AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
       AND (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002885') 
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000239')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002886')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000241')



GROUP BY
  Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)

"""