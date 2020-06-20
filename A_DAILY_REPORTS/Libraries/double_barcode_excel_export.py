#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd

def export(path_to_file,sql_answer):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter') as writer:
        sql_answer.to_excel(writer, sheet_name='Barcodes', startcol=0, startrow=0, index=None)

        # Φτιάχνω το excel για να είναι ευαναγνωστο
        workbook = writer.book
        worksheet = writer.sheets['Barcodes']
        number = workbook.add_format({'num_format': '€#,##0.00',
                                      'align': 'left',
                                      'bold': False,
                                      "font_name": "Avenir Next"})
        normal = workbook.add_format({
            'align': 'left',
            'bold': False,
            "font_name": "Avenir Next"})
        percent = workbook.add_format({'num_format': '%#,##0.00',
                                       'align': 'left',
                                       'bold': False,
                                       "font_name": "Avenir Next"})

        worksheet.set_column('A:A', 15, normal)
        worksheet.set_column('B:B', 15, normal)
        worksheet.set_column('C:C', 15, normal)
        worksheet.set_column('D:D', 15, number)
        worksheet.set_column('E:E', 15, number)

        # Conditional Formating
        worksheet.conditional_format('G1:G150', {'type': '3_color_scale'})