#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from datetime import datetime
def export(file_path, answer_01, answer_02, katastima):
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        # PUT ANSWERS INSIDE EXCEL
        answer_01.sort_values(by='Περιγραφή', ascending=True).to_excel(writer, sheet_name='NEW ORDER', startcol=0,
                                                                       startrow=4, index=None)

        # Get access to the workbook and sheet
        workbook = writer.book
        worksheet = writer.sheets['NEW ORDER']

        # Set the zoom a little
        worksheet.set_zoom(120)

        # SET BLUE Foreground on Cells
        set_color = workbook.add_format({'fg_color': '#ffdcd1',
                                         'align': 'center',
                                         # 'border': 1,
                                         'valign': 'vcenter',
                                         'num_format': '#,##0',
                                         'bold': False,
                                         "font_name": "Avenir Next"
                                         })
        # SET Another Foreground on Cells
        set_color_02 = workbook.add_format({'fg_color': '#8be1f0',
                                            'align': 'center',
                                            # 'border': 1,
                                            'valign': 'vcenter',
                                            'num_format': '#,##0',
                                            'text_wrap': True,
                                            'bold': False,
                                            "font_name": "Avenir Next"
                                            })
        # Center formatting
        center = workbook.add_format({'align': 'center',
                                      # 'border': 1,
                                      'valign': 'vcenter',
                                      'num_format': '#,##0',
                                      'text_wrap': True,
                                      'bold': False,
                                      "font_name": "Avenir Next"})
        # Left formatting
        left = workbook.add_format({'align': 'left',
                                    # 'border': 1,
                                    'valign': 'vcenter',
                                    'num_format': '#,##0',
                                    'bold': False,
                                    "font_name": "Avenir Next"})

        # FORMAT CELLS WIDTH
        worksheet.set_column('A:A', 20, center)
        worksheet.set_column('B:B', 50, left)
        worksheet.set_column('C:C', 10, center)
        worksheet.set_column('D:D', 10, center)

        # MERGE CELLS
        worksheet.merge_range("A1:D1", 'ΝΕΑ ΠΑΡΑΓΓΕΛΙΑ ΑΠΟ: ΚΟΥΤΟΥΛΑΚΗΣ Μ. ΑΤΣΑΛΗΣ Α. Ο.Ε.', set_color)
        worksheet.merge_range("A2:D2", 'Α.Φ.Μ. 082465475 || Υποκατάστημα: {}.'.format(katastima), set_color)
        worksheet.merge_range("A3:D3", 'ΠΡΟΣ: {}'.format(answer_02.Name[0]), set_color)
        worksheet.merge_range("A4:D4", 'Αριθμός Παραγγελίας: ({}) || ΗΜΕΡΟΜΗΝΙΑ: {}  '
                              .format(answer_02.Code[0], datetime.now().strftime("%d/%m/%Y")), set_color)
        worksheet.merge_range("E1:F4", "Συνολική Ποσότητα {} Τεμ.".format(sum(answer_01.Ποσότητα)), set_color_02)
        worksheet.merge_range("G1:H4", "Συνολικά Είδη          {}.".format(len(answer_01.Ποσότητα)), set_color_02)
