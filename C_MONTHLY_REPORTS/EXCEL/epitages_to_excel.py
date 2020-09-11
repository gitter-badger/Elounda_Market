#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd


def run(path_to_file, data):
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format=' dd - mm - yyyy') as writer:
        length = 1
        for i in data['ΤΡΑΠΕΖΑ'].unique():
            data[['ΑΡΙΘΜΟΣ ΕΠΙΤΑΓΗΣ', 'ΗΜΕΡΟΜΗΝΙΑ ΚΑΤΑΧΩΡΗΣΗΣ', 'ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ',
            'ΠΟΣΟ', 'ΕΠΩΝΥΜΙΑ', 'ΣΧΟΛΙΑ', 'ΑΝΟΙΧΤΟ']][data['ΤΡΑΠΕΖΑ'] == i].to_excel(writer, sheet_name='TODAY', startcol=0,
                                                         startrow=length, index=None)

            # Φτιάχνω το EXCEL για να είναι ευαναγνωστο
            workbook = writer.book
            worksheet = writer.sheets['TODAY']
            number = workbook.add_format({'num_format': '€#,##0.00',
                                          'align': 'left',
                                          'bold': True,
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

            worksheet.set_column('A:A', 25, normal)
            worksheet.set_column('B:B', 25, normal)
            worksheet.set_column('C:C', 25, normal)
            worksheet.set_column('D:D', 25, number)
            worksheet.set_column('E:E', 25, normal)
            worksheet.set_column('F:F', 25, normal)
            worksheet.set_column('G:G', 45, normal)

            worksheet.merge_range(f"A{length}:G{length}", f'{i}', center)

            length += len(data[data['ΤΡΑΠΕΖΑ'] == i]) + 3