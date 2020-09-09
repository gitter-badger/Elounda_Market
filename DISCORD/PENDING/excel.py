#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd


def run(path_to_file, tabs, answers):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format=' dd - mm - yyyy') as writer:
        for i, tab in enumerate(tabs):
            answers[i].to_excel(writer, sheet_name=tab, startcol=0, startrow=0, index=None)

            # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
            workbook = writer.book
            worksheet = writer.sheets[tab]
            # Formats
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
            # Fix Columns
            worksheet.set_column('A:A', 20, normal)
            worksheet.set_column('B:B', 15, normal)
            worksheet.set_column('C:C', 50, number)
            worksheet.set_column('D:D', 50, number)
            worksheet.set_column('E:E', 20, number)
            worksheet.set_column('F:F', 30, number)
            worksheet.set_column('G:G', 20, number)