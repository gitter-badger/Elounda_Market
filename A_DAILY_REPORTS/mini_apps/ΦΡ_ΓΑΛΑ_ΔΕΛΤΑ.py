#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from datetime import datetime
import pandas as pd
from Private import sql_connect,slack_app
import matplotlib.pyplot as plt
file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/Φρέσκο Γάλα Δέλτα POS.xlsx'

# -----------| SQL QUERY -------------
query = """
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
       AND (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002885') 
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000239')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-002886')
       OR (FK_ESFIItemPeriodics_ESFIItem.Code = '00-000241')



GROUP BY
  Year(FK_ESFIItemPeriodics_ESGOFiscalPeriod.BeginDate)

"""

# -------------Pandas GET Answer ------------
answer = pd.read_sql_query(query, sql_connect.sql_cnx())
answer_2 = pd.read_sql_query(query_2, sql_connect.sql_cnx())

X = answer_2['YEAR']
y = answer_2['TurnOver']
plt.figure(figsize=(15, 9))
plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ' , title= 'ELOUNDA MARKET (ΦΡΕΣΚΟ ΓΑΛΑ ΔΕΛΤΑ)')
colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
plt.bar(X, y, alpha=0.9, color=colors)
for a, b in zip(X, y):
    label = "{:.2f} €".format(b)

    # this method is called for each point
    plt.annotate(label,  # this is the text
                 (a, b),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
plt.grid(True, alpha=0.5)
plt.savefig('fresco_gala_delta_views.png')
# plt.show()

pl = 12
# Εισαγωγή Δεομένων στο  EXCEL
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    answer.to_excel(writer, sheet_name='ΦΡ_ΓΑΛΑ_ΔΕΛΤΑ', startcol=3, startrow=0)
    answer_2.to_excel(writer, sheet_name='ΦΡ_ΓΑΛΑ_ΔΕΛΤΑ', startcol=0, startrow=0)
    # Φτιάχνω το excel για να είναι ευαναγνωστο
    workbook = writer.book
    worksheet = writer.sheets['ΦΡ_ΓΑΛΑ_ΔΕΛΤΑ']
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

    # Conditional Formating
    worksheet.conditional_format('F2:F{}'.format(pl + 1), {'type': 'data_bar', 'bar_color': 'red'})
    worksheet.conditional_format('C2:C28', {'type': 'data_bar', 'bar_color': 'yellow'})
    worksheet.conditional_format('$G${}:$Z${}'.format(2, pl + 1), {'type': 'data_bar'})

    # MERGE CELLS
    worksheet.merge_range("M18:R18", 'ΤΕΛΕΥΑΤΑΙΑ ΕΝΗΜΕΡΩΣΗ', set_color)
    worksheet.merge_range("M19:R19", 'ΗΜΕΡΟΜΗΝΙΑ: {}  '.format(datetime.now().strftime("%d/%m/%Y")), set_color)
    worksheet.merge_range("M20:R20", 'ΩΡΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)

    # Φτιάχνω το Γράφημα
    chart02 = workbook.add_chart({'type': 'column'})
    chart02.add_series({'categories': '=ΦΡ_ΓΑΛΑ_ΔΕΛΤΑ!$B$2:$B$10',
                        'values': '=ΦΡ_ΓΑΛΑ_ΔΕΛΤΑ!$C$2:$C$10',
                        'name': 'ΕΤΗΣΙΟΣ ΤΖΙΡΟΣ'
                        })
    chart02.set_x_axis({'name': 'ΕΤΟΣ'})
    chart02.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
    chart02.set_size({'width': 1200, 'height': 900})
    worksheet.insert_chart('A15', chart02)


slack_app.send_text("""
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
`Ενημερώθηκε Το Αρχείο: Φρέσκο Γάλα Δέλτα POS.xlsx`
""", slack_app.channels[1])

slack_app.send_files('Φρέσκο Γάλα Δέλτα POS.xlsx', file_path, 'xlsx', slack_app.channels[1])
slack_app.send_files('fresco_gala_delta_views.png', 'fresco_gala_delta_views.png', 'png', slack_app.channels[1])
