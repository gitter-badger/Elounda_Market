#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd


def run(path_to_file, sql_answer):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format=' dd - mm - yyyy') as writer:
        sql_answer.to_excel(writer, sheet_name='CREDIT', startcol=0, startrow=0, index=None, header=True)

        # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
        workbook = writer.book
        worksheet = writer.sheets['CREDIT']
        number = workbook.add_format({'num_format': '€#,##0.00',
                                      'align': 'left',
                                      'bold': False,
                                      "font_name": "Avenir Next"})
        normal = workbook.add_format({
            'align': 'center',
            'bold': False,
            "font_name": "Avenir Next"})

        worksheet.set_column('A:A', 20, normal)
        worksheet.set_column('B:B', 30, normal)
        worksheet.set_column('C:C', 20, number)


        # Conditional Formating
        worksheet.conditional_format('C1:C150', {'type': '3_color_scale'})