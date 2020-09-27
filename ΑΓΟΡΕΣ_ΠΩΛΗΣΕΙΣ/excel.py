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
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})

        red_color = workbook.add_format({
            'fg_color': '#f5a593',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})
        green_color = workbook.add_format({
            'fg_color': '#7be88a',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})
        blue_color = workbook.add_format({
            'fg_color': '#82a9e0',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})
        purple_color = workbook.add_format({
            'fg_color': '#cb7bdb',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})
        yellow_color = workbook.add_format({
            'fg_color': '#e3e174',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})
        cyan_color = workbook.add_format({
            'fg_color': '#5cb0bf',
            'align': 'LEFT',
            'bold': False,
            "font_name": "Avenir Next"})

        worksheet.set_column('A:A', 15, normal)
        worksheet.set_column('B:B', 60, normal)
        worksheet.set_column('C:C', 10, red_color)
        worksheet.set_column('D:D', 10, red_color)
        worksheet.set_column('E:E', 10, green_color)
        worksheet.set_column('F:F', 10, green_color)
        worksheet.set_column('G:G', 10, blue_color)
        worksheet.set_column('H:H', 10, blue_color)
        worksheet.set_column('I:I', 10, purple_color)
        worksheet.set_column('J:J', 10, purple_color)
        worksheet.set_column('K:K', 10, yellow_color)
        worksheet.set_column('L:L', 10, yellow_color)
        worksheet.set_column('M:M', 10, cyan_color)
        worksheet.set_column('N:N', 10, cyan_color)




        # Conditional Formating
        #worksheet.conditional_format('C1:C150', {'type': '3_color_scale'})
