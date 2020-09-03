#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

#  ----Ονόματα προμηθευτών
def query_00():
    return "SELECT NAME FROM ESFITradeAccount where ESFITradeAccount.Type = 1 and Inactive= 0"

# -----------| SQL QUERY | All Years | All Months | TZIROS | SALES|----------------------------------
def query_01():
    return """
SELECT
    format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy') as 'YEAR'
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 1 then TurnOver end), 0) Jan
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2 then TurnOver end), 0) Feb
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 3 then TurnOver end), 0) Mar
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 4 then TurnOver end), 0) Apr
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 5 then TurnOver end), 0) May
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 6 then TurnOver end), 0) Jun
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 7 then TurnOver end), 0) Jul
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 8 then TurnOver end), 0) Aug
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 9 then TurnOver end), 0) Sep
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 10 then TurnOver end), 0) Oct
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 11 then TurnOver end), 0) Nov
  ,isnull(sum(case when month(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 12 then TurnOver end), 0) Dec
  ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver

 FROM ESFIItemPeriodics
     LEFT JOIN ESGOSites AS FK_ESFIItemPeriodics_ESGOSites
       ON ESFIItemPeriodics.fSiteGID = FK_ESFIItemPeriodics_ESGOSites.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFIItemPeriodics_ESGOFiscalPeriod
       ON ESFIItemPeriodics.fFiscalPeriodGID = FK_ESFIItemPeriodics_ESGOFiscalPeriod.GID
     WHERE
        (FK_ESFIItemPeriodics_ESGOSites.Code = '1')
GROUP BY

        format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy')
order by
        format(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'yyyy')
"""


# sales
def query(inputs):
    q = """

    SELECT
       IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'') 
        AS SubCategory
        ,Sum(ESFIItemPeriodics.TurnOver) AS TurnOver
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2012 then TurnOver end), 0) as 'f2012'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2013 then TurnOver end), 0) as 'f2013'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2014 then TurnOver end), 0) as 'f2014'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2015 then TurnOver end), 0) as 'f2015'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2016 then TurnOver end), 0) as 'f2016'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2017 then TurnOver end), 0) as 'f2017'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2018 then TurnOver end), 0) as 'f2018'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2019 then TurnOver end), 0) as 'f2019'
    ,isnull(sum(case when Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) = 2020 then TurnOver end), 0) as 'f2020'


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
       AND (FK_ESFIItemPeriodics_ESGOSites.Code = 1) -- Υποκατάστημα (1) Κεντρικά Έδρας
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemSubcategoryCode in {}) -- Υποκατηγορία (είσοδος)

    GROUP BY
 -- FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate,
    IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'')  --  (Brand Name group)

""".format(inputs)
    return q


def count_query(inputs):
    q = """
    SELECT
      count(*)
    FROM  ESFIItem 
        WHERE    
       (ESFIItem.fItemSubcategoryCode in {})
""".format(inputs)
    return q


# ----------- Προμηθευτές -------------------
def querry_suppliers(input):
    q = """
      SELECT
    FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name AS 'Επωνυμία'
    ,Sum(ESFITradeAccountPeriodics.NumberOfInvoices) AS 'Ποσότητα Τιμολογίων'
    ,Sum(ESFITradeAccountPeriodics.NumberOfCreditNotes) AS 'Ποσότητα Πιστωτικών'
    ,Sum(ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover) AS 'Τζίρος'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2012 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2012'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2013 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2013'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2014 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2014'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2015 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2015'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2016 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2016'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2017 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2017'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2018 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2018'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2019 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2019'
    ,isnull(sum(case when Year(FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.BeginDate) = 2020 then ESFITradeAccountPeriodics.Turnover-ESFITradeAccountPeriodics.SponsionTurnover end), 0) as 'f2020'

FROM ESFITradeAccountPeriodics AS ESFITradeAccountPeriodics
     LEFT JOIN ESFITradeAccount AS FK_ESFITradeAccountPeriodics_ESFITradeAccount
       ON ESFITradeAccountPeriodics.fTradeAccountGID = FK_ESFITradeAccountPeriodics_ESFITradeAccount.GID
     LEFT JOIN ESGOSites AS FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite
       ON ESFITradeAccountPeriodics.fTradeAccountSiteGID = FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite.GID
     LEFT JOIN ESGOSites AS FK_ESFITradeAccountPeriodics_ESGOSites_Site
       ON ESFITradeAccountPeriodics.fSiteGID = FK_ESFITradeAccountPeriodics_ESGOSites_Site.GID
     LEFT JOIN ESGOFiscalPeriod AS FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod
       ON ESFITradeAccountPeriodics.fFiscalPeriodGID = FK_ESFITradeAccountPeriodics_ESGOFiscalPeriod.GID
     LEFT JOIN ESGOFiscalYear AS FK_ESFITradeAccountPeriodics_ESGOFiscalYear
       ON ESFITradeAccountPeriodics.fFiscalYearGID = FK_ESFITradeAccountPeriodics_ESGOFiscalYear.GID
     LEFT JOIN ESGOPerson AS FK_ESGOPerson_PersonCode1
       ON FK_ESFITradeAccountPeriodics_ESFITradeAccount.fPersonCodeGID = FK_ESGOPerson_PersonCode1.GID
     LEFT JOIN ESFIZTradeAccountFamily AS FK_ESFITradeAccount_ESFIZTradeAccountFamily
       ON FK_ESFITradeAccountPeriodics_ESFITradeAccount.fFamilyCode = FK_ESFITradeAccount_ESFIZTradeAccountFamily.Code
     LEFT JOIN ESGOZRegionGroup AS FK_ESGOSites_ESGOZRegionGroup
       ON FK_ESFITradeAccountPeriodics_ESGOSites_TradeAccountSite.fRegionGroupCode = FK_ESGOSites_ESGOZRegionGroup.Code
     LEFT JOIN ESGOZGroup AS FK_ESGOPerson_ESGOZGroup
       ON FK_ESGOPerson_PersonCode1.fGroupCode = FK_ESGOPerson_ESGOZGroup.Code
     LEFT JOIN ESGOZCategory AS FK_ESGOPerson_ESGOZCategory
       ON FK_ESGOPerson_PersonCode1.fCategoryCode = FK_ESGOPerson_ESGOZCategory.Code
     LEFT JOIN ESGOZActivity AS FK_ESGOPerson_ESGOZActivity
       ON FK_ESGOPerson_PersonCode1.fActivityCode = FK_ESGOPerson_ESGOZActivity.Code
WHERE
        (ESFITradeAccountPeriodics.TradeAccountType in (1,3))
       AND (FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name  in {}) -- tuple με προμθευτές (είσοδος)
       AND (ESFITradeAccountPeriodics.Turnover > 0) --  Τζίρος > 0
       and FK_ESFITradeAccountPeriodics_ESGOSites_Site.Code = 1 -- Υποκατάστημα (1) Κεντρικά Έδρας


GROUP BY FK_ESFITradeAccountPeriodics_ESFITradeAccount.Name
order by 4  desc
    """.format(input)
    return q
