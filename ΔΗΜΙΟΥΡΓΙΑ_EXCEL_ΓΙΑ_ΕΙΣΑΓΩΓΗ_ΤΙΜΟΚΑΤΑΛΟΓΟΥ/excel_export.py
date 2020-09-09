#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd


def export(path_to_file, sql_answer):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format='dd - mm - yyyy') as writer:
        sql_answer.to_excel(writer, sheet_name='TODAY', startcol=0, startrow=0, index=None)

        # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
        workbook = writer.book
        worksheet = writer.sheets['TODAY']
        number = workbook.add_format({'num_format': '€#,##0.00',
                                      'align': 'left',
                                      'bold': False,
                                      "font_name": "Avenir Next"})

        normal = workbook.add_format({'align': 'left',
                                      'bold': False,
                                      "font_name": "Avenir Next"})

        percent = workbook.add_format({'num_format': '%#,##0.00',
                                       'align': 'left',
                                       'bold': False,
                                       "font_name": "Avenir Next"})

        worksheet.set_column('A:A', 15, normal)
        worksheet.set_column('B:B', 15, normal)
        worksheet.set_column('C:C', 50, normal)
        worksheet.set_column('D:D', 15, normal)
        worksheet.set_column('E:E', 10, normal)
        worksheet.set_column('F:F', 50, normal)
        worksheet.set_column('G:G', 12, number)
        worksheet.set_column('H:H', 12, number)
        worksheet.set_column('I:I', 12, percent)
        worksheet.set_column('J:J', 12, number)
        worksheet.set_column('K:K', 12, number)
        worksheet.set_column('L:L', 12, number)

        # Conditional Formating
        worksheet.conditional_format('I1:I500', {'type': '3_color_scale'})
