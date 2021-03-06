#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd


def export(path_to_file, sql_answer):
    sql_answer = sql_answer.sort_values(by=['BRAND', 'ΠΕΡΙΓΡΑΦΗ'])
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter') as writer:
        length = 1
        for i in sql_answer['BRAND'].unique():
            sql_answer[sql_answer['BRAND'] == i].to_excel(writer, sheet_name='TODAY', startcol=0, startrow=length,
                                                          index=None)

            # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
            workbook = writer.book
            worksheet = writer.sheets['TODAY']
            number = workbook.add_format({
                'num_format': '€#,##0.00',
                'align': 'left',
                'bold': False,
                "font_name": "Avenir Next"})
            normal = workbook.add_format({
                'align': 'left',
                'bold': False,
                "font_name": "Avenir Next"})
            percent = workbook.add_format({
                'num_format': '%#,##0.00',
                'align': 'left',
                'bold': False,
                "font_name": "Avenir Next"})
            center = workbook.add_format({
                'align': 'center',
                'fg_color': '#ffdcd1',
                'bold': True,
                "font_name": "Avenir Next"})

            worksheet.set_column('A:A', 0, normal)  # ΠΑΡΑΣΤΑΤΙΚΟ
            worksheet.set_column('B:B', 13, normal)  # BARCODE
            worksheet.set_column('C:C', 40, normal)  # ΠΕΡΙΓΡΑΦΗ
            worksheet.set_column('D:D', 0, normal)  # ΥΠΟΚΑΤΗΓΟΡΙΑ
            worksheet.set_column('E:E', 10, normal)  # ΠΟΣΟΤΗΤΑ
            worksheet.set_column('F:F', 12, number)  # ΚΑΘΑΡΗ ΤΙΜΗ
            worksheet.set_column('G:G', 12, number)  # ΤΙΜΗ ΛΙΑΝΙΚΗΣ
            worksheet.set_column('H:H', 10, percent)  # ΚΕΡΔΟΦΟΡΙΑ
            worksheet.set_column('I:I', 12, number)  # ΤΙΜΗ BAZAAR
            worksheet.set_column('J:J', 18, number)  # TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ
            worksheet.set_column('K:K', 18, number)  # TIMH Care Market

            # Conditional Formating
            worksheet.conditional_format('H1:H1500', {'type': '3_color_scale'})
            mean_markup = round(sql_answer['ΚΕΡΔΟΦΟΡΙΑ'][sql_answer['BRAND'] == i].mean() * 100, 2)
            worksheet.merge_range(f"A{length}:K{length}", f'BRAND NAME: {i} MARKUP: {mean_markup}', center)

            length += len(sql_answer[sql_answer['BRAND'] == i]) + 3
