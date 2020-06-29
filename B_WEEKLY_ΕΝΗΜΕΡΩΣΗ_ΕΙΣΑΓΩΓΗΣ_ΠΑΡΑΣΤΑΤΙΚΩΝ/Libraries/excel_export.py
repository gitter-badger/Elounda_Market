#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd

def export(path_to_file, final_result):
    # -------------------- IMPORT DATA TO EXCEL --------------------
    with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format='dd - mm - yyyy') as writer:
        length = 1
        for i in final_result['BRAND'].unique():
            final_result[final_result['BRAND'] == i].to_excel(writer, sheet_name='TODAY', startcol=0, startrow=length, index=None)


            # Φτιάχνω το excel για να είναι ευαναγνωστο
            workbook = writer.book
            worksheet = writer.sheets['TODAY']

            normal = workbook.add_format({'align': 'left',
                                          'bold': False,
                                          "font_name": "Avenir Next"})
            center = workbook.add_format({'align': 'center',
                                          'fg_color': '#ffdcd1',
                                          'bold': True,
                                          "font_name": "Avenir Next"})


            worksheet.set_column('A:A', 50, normal)
            worksheet.set_column('B:B', 20, normal)
            worksheet.merge_range(f"A{length}:C{length}", f'{i}', center)

            length += len(final_result[final_result['BRAND'] == i]) + 3



