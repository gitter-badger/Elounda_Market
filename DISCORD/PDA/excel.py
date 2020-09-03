#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from datetime import datetime


def export(path, answer_01, answer_02, answer_03, answer_04, answer_05, answer_06):
    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
        # Εισαγωγή Δεδομένων στο Excel σε συγκεκριμένο Φύλλο και Θέση ---------------
        answer_01.to_excel(writer, sheet_name='PDA', startcol=0, startrow=1)
        answer_02.to_excel(writer, sheet_name='PDA', startcol=0, startrow=16)
        answer_03.to_excel(writer, sheet_name='PDA', startcol=5, startrow=1)
        answer_04.to_excel(writer, sheet_name='PDA', startcol=10, startrow=1)
        answer_05.to_excel(writer, sheet_name='PDA', startcol=10, startrow=16)
        answer_06.to_excel(writer, sheet_name='PDA', startcol=0, startrow=31)

        # ----ACCESS SPREAD AND SHEET ---------------------------------------------
        workbook = writer.book
        worksheet = writer.sheets['PDA']

        # ---- SPREADSHEET ZOOM ----------------------------------------------------
        worksheet.set_zoom(90)

        # ---- GENERAL FORMATING ----------------------------------------------------
        total_fmt = workbook.add_format({'align': 'right', 'num_format': '#,##0',
                                         'bold': True, 'bottom': 6})

        # ---- CENTERED FORMATING ----------------------------------------------------
        center = workbook.add_format({'align': 'center',
                                      'num_format': '#,##0',
                                      'bold': False,
                                      "font_name": "Poiret One",
                                      "font_size": 20})

        # ---- MONEY FORMAT ----------------------------------------------------------
        money_fmt = workbook.add_format({'num_format': '#,##0',
                                         'align': 'center',
                                         'bold': False,
                                         "font_name": "Avenir Next"})

        # ---- SET  Foreground Color on Cells -------------------------------------------
        set_color = workbook.add_format({'fg_color': '#ffdcd1',
                                         'align': 'center',
                                         # 'border': 1,
                                         'valign': 'vcenter',
                                         'num_format': '#,##0',
                                         'bold': False,
                                         "font_name": "Avenir Next"
                                         })

        # ---- CELL WIDTH ----------------------------------------------------------
        worksheet.set_column('B:D', 20, money_fmt)
        worksheet.set_column('A:A', 4, money_fmt)
        worksheet.set_column('E:F', 4, money_fmt)
        worksheet.set_column('J:K', 4, money_fmt)
        worksheet.set_column('G:I', 20, money_fmt)
        worksheet.set_column('L:N', 20, money_fmt)

        # ---- Conditional Formating --------------------------------------------------
        worksheet.conditional_format('N3:N15', {'type': '3_color_scale'})

        # ---- CHART 01 ----------------------------------------------------------------
        chart01 = workbook.add_chart({'type': 'column'})
        chart01.set_chartarea({'border': {'none': True},
                               'fill': {'color': '#c9e2f2'}
                               })
        chart01.set_plotarea({'border': {'none': True},
                              'fill': {'color': '#c9e2f2'}
                              })
        chart01.add_series({'values': '==PDA!$N$3:$N$14'})
        chart01.set_x_axis({'name': 'Month'})
        chart01.set_y_axis({'name': 'Count'})
        chart01.set_title({'name': 'All Stores Monthly', "font_name": "Gilbert Color"})
        worksheet.insert_chart('O2', chart01)

        # ---- CHART 02 ----------------------------------------------------------------
        chart02 = workbook.add_chart({'type': 'column'})
        chart02.set_chartarea({'border': {'none': True},
                               'fill': {'color': '#c9e2f2'}
                               })
        chart02.set_plotarea({'border': {'none': True},
                              'fill': {'color': '#c9e2f2'}
                              })
        chart02.add_series({'categories': '=PDA!$L$18:$L$23',
                            'values': '==PDA!$N$18:$N$23'})
        chart02.set_x_axis({'name': 'Year'})
        chart02.set_y_axis({'name': 'Count'})
        chart02.set_title({'name': 'All Stores Yearly', "font_name": "Gilbert Color"})
        worksheet.insert_chart('O18', chart02)

        # ---- CHART 03 ----------------------------------------------------------------
        chart03 = workbook.add_chart({'type': 'line'})
        chart03.set_chartarea({'border': {'none': True},
                               'fill': {'color': '#c9e2f2'}
                               })
        chart03.set_plotarea({'border': {'none': True},
                              'fill': {'color': '#c9e2f2'}
                              })
        chart03.add_series({'categories': '=PDA!$B$33:$B$50',
                            'values': '==PDA!$D$33:$D$50'})
        chart03.set_x_axis({'name': 'HOUR'})
        chart03.set_y_axis({'name': 'Count'})
        chart03.set_title({'name': 'Most Active Hours', "font_name": "Gilbert Color"})
        chart03.set_size({'x_scale': 2, 'y_scale': 1.5})
        worksheet.insert_chart('F32', chart03)

        # ---- INSERT IMAGES ----------------------------------------------------------
        # worksheet.insert_image('A01', 'sap.png', {'x_scale': 0.1, 'y_scale': 0.1})

        # ---- MERGE CELLS ------------------------------------------------------------
        worksheet.merge_range('A1:D1', 'All Stores | Today', center)
        worksheet.merge_range('A16:D16', 'All Stores | Hourly', center)
        worksheet.merge_range('G1:I1', 'All Stores | Daily', center)
        worksheet.merge_range('L1:N1', 'All Stores | Monthly', center)
        worksheet.merge_range('L16:N16', 'All Stores | Yearly', center)
        worksheet.merge_range('A31:D31', 'Most Active Hours', center)

        # MERGE CELLS IMPORT TIMESTAMP ----------------------------------------------------
        worksheet.merge_range("O35:T35", 'ΤΕΛΕΥΑΤΑΙΑ ΕΝΗΜΕΡΩΣΗ', set_color)
        worksheet.merge_range("O36:T36", 'ΗΜΕΡΟΜΗΝΙΑ: {}  '.format(datetime.now().strftime("%d/%m/%Y")), set_color)
        worksheet.merge_range("O37:T37", 'ΩΡΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)
