#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from datetime import datetime
import pandas as pd


def run(file_path, answer, answer_2, pl):
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