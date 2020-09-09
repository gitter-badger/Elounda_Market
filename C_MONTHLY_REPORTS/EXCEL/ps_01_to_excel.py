#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import datetime

def run(path_to_file, sql_answer):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format=' dd - mm - yyyy') as writer:
        length = 1
        for i in sql_answer['ΕΝΑΡΞΗ'].unique():
            sql_answer[sql_answer['ΕΝΑΡΞΗ'] == i].to_excel(writer, sheet_name='TODAY', startcol=0, startrow=length,
                                                          index=None)

            # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
            workbook = writer.book
            worksheet = writer.sheets['TODAY']
            number = workbook.add_format({'num_format': '€#,##0.00',
                                          'align': 'left',
                                          'bold': False,
                                          "font_name": "Avenir Next"})
            normal = workbook.add_format({
                'align': 'left',
                'bold': False,
                "font_name": "Avenir Next"})

            center = workbook.add_format({
                'align': 'center',
                'fg_color': '#ffdcd1',
                'bold': True,
                "font_name": "Avenir Next"})

            worksheet.set_column('A:A', 20, normal)
            worksheet.set_column('B:B', 20, normal)
            worksheet.set_column('C:C', 12, normal)
            worksheet.set_column('D:D', 12, normal)
            worksheet.set_column('E:E', 70, normal)
            worksheet.set_column('F:F', 15, normal)
            worksheet.set_column('G:G', 15, number)
            worksheet.set_column('H:H', 10, number)
            worksheet.set_column('I:I', 10, number)
            worksheet.set_column('J:J', 10, normal)

            worksheet.merge_range(f"A{length}:I{length}", f'ΠΑΚΕΤΟ ΠΡΟΣΦΟΡΑΣ', center)

            length += len(sql_answer[sql_answer['ΕΝΑΡΞΗ'] == i]) + 3
