#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from datetime import datetime
import pandas as pd


def run(output_file, answer, answer_01, answer_count, c, promi8eutes_list, answer_prom, answer_prom_count,
        kataskevastes_lst, answer_quant, answer_sum, year_2012, year_2013, year_2014, year_2015, year_2016,
        year_2017, year_2018, year_2019, year_2020):
    # -------------OPEN FILE | WRITE ----------------------------
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:  # doctest: +SKIP
        # PUT ANSWERS INSIDE EXCEL
        answer_01.to_excel(writer, sheet_name='YEAR', startcol=0, startrow=1)
        print(f'\n 07: Πωλήσεις εγγραφή στο  Excel --> Ολοκληρώθηκε: {datetime.now().strftime("%H:%M:%S")}')
        k = 2
        for i in range(len(c)):
            percent = int((100 * (i + 1)) / len(c))
            filler = "█" * percent
            remaining = '-' * (100 - percent)
            answer[i].to_excel(writer, sheet_name='ΚΑΤΑΣΚΕΥΑΣΤΗΣ', startcol=0, startrow=k)
            k += (4 + answer_count[i])
            print(f'\r 08: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)
        excel_positioning = 1
        print()
        # Προμηθευτές
        for i in range(len(promi8eutes_list)):
            percent = int((100 * (i + 1)) / len(promi8eutes_list))
            filler = "█" * percent
            remaining = '-' * (100 - percent)
            answer_prom[i].to_excel(writer, sheet_name='ΠΡΟΜΗΘΕΥΤΕΣ', startcol=0, startrow=excel_positioning)
            excel_positioning += (4 + answer_prom_count[i])
            print(f'\r 09: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

        print(f'\n 10: Προμηθευτές εγγραφή στο  Excel --> Ολοκληρώθηκε: {datetime.now().strftime("%H:%M:%S")}')
        # Get access to the workbook and sheet
        workbook = writer.book
        worksheet = writer.sheets['YEAR']
        worksheet_2 = writer.sheets['ΚΑΤΑΣΚΕΥΑΣΤΗΣ']
        worksheet_3 = workbook.add_worksheet('ΓΡΑΦΗΜΑΤΑ')
        worksheet_4 = writer.sheets['ΠΡΟΜΗΘΕΥΤΕΣ']
        worksheet_5 = workbook.add_worksheet('ΣΥΝΟΠΤΙΚΑ')

        # Reduce the zoom a little
        worksheet.set_zoom(90)
        # Center formatting
        center = workbook.add_format({'align': 'center',
                                      # 'border': 1,
                                      'valign': 'vcenter',
                                      'num_format': '#,##0',
                                      'bold': False,
                                      "font_name": "Avenir Next"})

        # Add a number format for cells with money.
        money_fmt = workbook.add_format({'num_format': '€#,##0.00',
                                         'align': 'center',
                                         'bold': False,
                                         "font_name": "Avenir Next"})
        # SET BLUE Foreground on Cells
        set_color = workbook.add_format({'fg_color': '#ffdcd1',
                                         'align': 'center',
                                         # 'border': 1,
                                         'valign': 'vcenter',
                                         'num_format': '#,##0',
                                         'bold': False,
                                         "font_name": "Avenir Next"
                                         })

        # FORMAT CELLS WIDTH
        worksheet.set_column('C:O', 15, money_fmt)
        worksheet.set_column('A:B', 15, center)
        worksheet_2.set_column('A:A', 5, center)
        worksheet_2.set_column('B:W', 15, money_fmt)
        worksheet_4.set_column('A:A', 5, center)
        worksheet_4.set_column('B:B', 40, center)
        worksheet_4.set_column('C:D', 20, center)
        worksheet_4.set_column('E:O', 20, money_fmt)
        print(f'\n 11: Format EXCEL --> Ολοκληρώθηκε:  {datetime.now().strftime("%H:%M:%S")}', end='')
        # MERGE CELLS
        worksheet.merge_range("M14:R14", 'ΤΕΛΕΥΑΤΑΙΑ ΕΝΗΜΕΡΩΣΗ', set_color)
        worksheet.merge_range("M15:R15", 'ΗΜΕΡΟΜΗΝΙΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)
        worksheet.merge_range("M16:R16", 'ΩΡΑ: {}  '.format(datetime.now().strftime("%H:%M:%S")), set_color)
        print(f'\n 12: MERGING CELLS --> Ολοκληρώθηκε:  {datetime.now().strftime("%H:%M:%S")}', end='')
        # Conditional Formating
        worksheet.conditional_format('O1:O15', {'type': '3_color_scale'})
        print(f'\n 13: Conditional Formating --> Ολοκληρώθηκε:  {datetime.now().strftime("%H:%M:%S")}', end='')
        # CHARTS
        chart01 = workbook.add_chart({'type': 'column'})
        chart01.add_series({'categories': '=YEAR!$B$3:$B$11',
                            'values': '=YEAR!$O$3:$O$11',
                            'data_labels': {'value': True,
                                            'position': 'outside_end'
                                            },
                            'name': 'ΤΖΙΡΟΣ'
                            }, )
        chart01.set_x_axis({'name': 'YEAR'})
        chart01.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
        chart01.set_size({'width': 1100, 'height': 300})
        worksheet.insert_chart('A12', chart01)
        print(f'\n 14: CHARTS INSIDE EXCEL --> Ολοκληρώθηκε:  {datetime.now().strftime("%H:%M:%S")}')
        # Counters για τα Γραφήματα
        a = []
        b = []
        for i in range(0, 900, 13):
            for j in range(0, 22, 7):
                a.append(i)
                b.append(j)

        print(f'\n 15: Counters για τα Γραφήματα --> Ολοκληρώθηκε:  {datetime.now().strftime("%H:%M:%S")}')

        # Function CHART
        def chart(i, j, k):
            chart02 = workbook.add_chart({'type': 'column'})
            chart02.add_series({'categories': '=ΚΑΤΑΣΚΕΥΑΣΤΗΣ!$D$3:$L$3',
                                'values': '=ΚΑΤΑΣΚΕΥΑΣΤΗΣ!$D${}:$L${}'.format(j, j),
                                'name': '{}'.format(kataskevastes_lst[i])
                                }, )
            chart02.set_x_axis({'name': 'YEAR'})
            chart02.set_y_axis({'name': 'ΤΖΙΡΟΣ'})
            chart02.set_legend({'position': 'none'})
            chart02.set_size({'width': 400, 'height': 250})
            # worksheet_2.insert_chart('M{}'.format(k), chart02)
            worksheet_3.insert_chart(a[i], b[i], chart02)

        # Function MERGE CELLS
        def w(number, lista, count, sumi):
            worksheet_2.merge_range("A{}:D{}".format(number, number), '{}'.format(kataskevastes_lst[lista]), set_color)
            worksheet_2.merge_range("E{}:F{}".format(number, number), 'Πλήθος Κωδικών:', set_color)
            worksheet_2.merge_range("G{}:H{}".format(number, number), '{}'.format(count), set_color)
            worksheet_2.merge_range("I{}:J{}".format(number, number), 'Τζίρος:', set_color)
            worksheet_2.merge_range("K{}:L{}".format(number, number), '{}€'.format(round(sumi, 2)), set_color)
            worksheet_2.merge_range("A{}:L{}".format(number + 1, number + 1), '{}'.format(c[i]), set_color)

        j = 1
        k = 1
        row_num = 0
        col_num = 0
        for i in range(len(c)):
            percent = int((100 * (i + 1)) / len(c))
            filler = "█" * percent
            remaining = '-' * (100 - percent)
            worksheet_2.conditional_format('C{}:C{}'.format(j + 3, j + 3 + answer_count[i]), {'type': 'data_bar'})
            w(j, i, answer_quant[i].values, answer_sum[i])
            j += (answer_count[i] + 2)
            worksheet_2.write(j, 3, year_2012[i])
            worksheet_2.write(j, 4, year_2013[i])
            worksheet_2.write(j, 5, year_2014[i])
            worksheet_2.write(j, 6, year_2015[i])
            worksheet_2.write(j, 7, year_2016[i])
            worksheet_2.write(j, 8, year_2017[i])
            worksheet_2.write(j, 9, year_2018[i])
            worksheet_2.write(j, 10, year_2019[i])
            worksheet_2.write(j, 11, year_2020[i])
            j += 1
            chart(i, j, k)
            j += 1
            k += 10
            print(f'\r 16: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

        print()

        # Προμηθευτές
        def fun_suppliers(input):
            worksheet_4.merge_range('$A${}:$M${}'.format(input, input),
                                    'Επιλεγμένη Λίστα Προμηθευτών', set_color)

        prom_counter = 1
        for i in range(len(promi8eutes_list)):
            percent = int((100 * (i + 1)) / len(promi8eutes_list))
            filler = "█" * percent
            remaining = '-' * (100 - percent)
            worksheet_4.conditional_format('C{}:C{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                           {'type': 'data_bar', 'bar_color': 'blue'})
            worksheet_4.conditional_format('D{}:D{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                           {'type': 'data_bar', 'bar_color': 'green'})
            worksheet_4.conditional_format('E{}:E{}'.format(prom_counter + 2, prom_counter + 2 + answer_prom_count[i]),
                                           {'type': 'data_bar', 'bar_color': 'red'})
            fun_suppliers(prom_counter)
            prom_counter += (answer_prom_count[i] + 4)
            print(f'\r 17: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)
        print()
        # Συνοπτικά
        worksheet_5.write(0, 0, 'Κατασκευαστής')
        j = 2012
        for i in range(1, 9):
            percent = int((100 * i) / 8)
            filler = "█" * percent
            remaining = '-' * (100 - percent)
            worksheet_5.write(0, i, '{}'.format(j))
            j += 1
            print(f'\r 18: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)
        print()
        j = 1
        for i in range(len(c)):
            percent = int((100 * (i + 1)) / len(c))
            filler = "█" * percent
            remaining = '-' * (100 - percent)

            worksheet_5.write(j, 0, kataskevastes_lst[i])
            worksheet_5.write(j, 1, year_2012[i])
            worksheet_5.write(j, 2, year_2013[i])
            worksheet_5.write(j, 3, year_2014[i])
            worksheet_5.write(j, 4, year_2015[i])
            worksheet_5.write(j, 5, year_2016[i])
            worksheet_5.write(j, 6, year_2017[i])
            worksheet_5.write(j, 7, year_2018[i])
            worksheet_5.write(j, 8, year_2019[i])
            worksheet_5.write(j, 9, year_2020[i])
            j += 1
            print(f'\r 19: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

        # INSERT IMAGES
        # worksheet.insert_image('A27', 'sap.png', {'x_scale': 0.2, 'y_scale': 0.2})
        # worksheet.insert_image('I27', 'crystal.png', {'x_scale': 0.27, 'y_scale': 0.29})
    print()
