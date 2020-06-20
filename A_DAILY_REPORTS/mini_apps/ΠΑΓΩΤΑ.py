#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from datetime import datetime
import pandas as pd
from Private import sql_connect,slack_app
import matplotlib.pyplot as plt
file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/Παγωτά.xlsx'

# -----------| SQL QUERY -------------
query = """
SELECT
       IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'') 
        AS SubCategory
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
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemCategoryCode = '00-09-05')

GROUP BY
 -- FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate,
 IsNull(FK_ESFIItemPeriodics_ESFIItem.fItemSubCategoryCode,'') 
"""

query_2 = """
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
       AND (FK_ESFIItemPeriodics_ESFIItem.fItemCategoryCode = '00-09-05')



GROUP BY
  Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)

"""

query_03 = """
select 
count(distinct(ESFIItem.fItemSubcategoryCode)) as count from ESFIItem
where ESFIItem.fItemCategoryCode = '00-09-05'
"""

# -------------Pandas GET Answer ------------
answer = pd.read_sql_query(query, sql_connect.sql_cnx())
answer_2 = pd.read_sql_query(query_2, sql_connect.sql_cnx())
answer_3 = pd.read_sql_query(query_03, sql_connect.sql_cnx())
pl = answer_3.values.min()

X = answer_2['YEAR']
y = answer_2['TurnOver']
plt.figure(figsize=(15, 9))
plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ' , title= 'ELOUNDA MARKET (ΠΑΓΩΤΑ)')
plt.bar(X, y, alpha=0.5)
for a, b in zip(X, y):
    label = "{:.2f} €".format(b)

    # this method is called for each point
    plt.annotate(label,  # this is the text
                 (a, b),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
plt.grid(True, alpha=0.5)
plt.savefig('pagota_views.png')
plt.show()


# Εισαγωγή Δεομένων στο  EXCEL
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    answer.to_excel(writer, sheet_name='ΠΑΓΩΤΑ', startcol=3, startrow=0)
    answer_2.to_excel(writer, sheet_name='ΠΑΓΩΤΑ', startcol=0, startrow=0)
    # Φτιάχνω το excel για να είναι ευαναγνωστο
    workbook = writer.book
    worksheet = writer.sheets['ΠΑΓΩΤΑ']
    number = workbook.add_format({'num_format': '€#,##0.00',
                                  'align': 'left',
                                  'bold': False,
                                  "font_name": "Avenir Next"})
    normal = workbook.add_format({
        'align': 'left',
        'bold': False,
        "font_name": "Avenir Next"})

    # SET BLUE Foreground on Cells
    set_color = workbook.add_format({'fg_color': '#ffdcd1',
                                     'align': 'center',
                                     # 'border': 1,
                                     'valign': 'vcenter',
                                     'num_format': '#,##0',
                                     'bold': False,
                                     "font_name": "Avenir Next"
                                     })

    worksheet.set_column('A:A', 2, number)
    worksheet.set_column('B:B', 10, normal)
    worksheet.set_column('C:C', 15, number)
    worksheet.set_column('D:D', 2, number)
    worksheet.set_column('E:E', 30, number)
    worksheet.set_column('F:F', 15, number)
    worksheet.set_column('G:G', 15, number)
    worksheet.set_column('H:H', 15, number)
    worksheet.set_column('I:I', 15, number)
    worksheet.set_column('J:J', 15, number)
    worksheet.set_column('K:K', 15, number)
    worksheet.set_column('L:P', 15, number)

    # Αλλάζω το Zoom από 100% σε 90%
    worksheet.set_zoom(90)

    # MERGE CELLS
    worksheet.merge_range("M35:R35", 'ΤΕΛΕΥΑΤΑΙΑ ΕΝΗΜΕΡΩΣΗ', set_color)
    worksheet.merge_range("M36:R36", 'ΗΜΕΡΟΜΗΝΙΑ: {}  '.format(datetime.now().strftime("%d/%m/%Y")), set_color)
    worksheet.merge_range("M37:R37", 'ΩΡΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)

    # Conditional Formating
    worksheet.conditional_format('F2:F{}'.format(pl + 1), {'type': 'data_bar', 'bar_color': 'red'})
    worksheet.conditional_format('C2:C28', {'type': 'data_bar', 'bar_color': 'yellow'})
    worksheet.conditional_format('$G${}:$Z${}'.format(2, pl + 1), {'type': 'data_bar'})

    # Φτιάχνω το Γράφημα
    chart02 = workbook.add_chart({'type': 'column'})
    chart02.add_series({'categories': '=ΠΑΓΩΤΑ!$B$2:$B$10',
                        'values': '=ΠΑΓΩΤΑ!$C$2:$C$10',
                        'name': 'ΕΤΗΣΙΟΣ ΤΖΙΡΟΣ'
                        })
    chart02.set_x_axis({'name': 'ΕΤΟΣ'})
    chart02.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
    chart02.set_size({'width': 1200, 'height': 900})
    worksheet.insert_chart('A32', chart02)

slack_app.send_text("""
>ΤΑΚΤΙΚΑ ΑΡΧΕΙΑ
`Ενημερώθηκε Το Αρχείο: Παγωτά.xlsx`
""", slack_app.channels[1])

slack_app.send_files('Παγωτά.xlsx', file_path, 'xlsx', slack_app.channels[1])
slack_app.send_files('pagota_views.png', 'pagota_views.png', 'png', slack_app.channels[1])
