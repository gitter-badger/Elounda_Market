#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
def sales_per_category(category):
    return f"""
SELECT
     FORMAT(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'MM-MMM') AS MONTH,
     Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate) as 'YEAR',
     Sum(ESFIItemPeriodics.TurnOver) AS TurnOver

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
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemCategoryCode in {category})



GROUP BY
Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate),
FORMAT(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate, 'MM-MMM')
"""
