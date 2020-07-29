#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ.library import sql_select, timokatalogos, excel_export
from Private import sql_connect, slack_app
import matplotlib.pyplot as plt
import time
from datetime import datetime as dt
import numpy as np
import squarify

# ---------------- MAKE DF REPORT VIEWABLE ----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- SLACK DELETE ALL --------------------
# x = (slack_app.history(slack_app.channels_id[0]))
# for i in range(len(x['messages'])):
#     timer = (x['messages'][i]['ts'])
#     slack_app.delete(slack_app.channels_id[0], timer)

# -------------------- STATEMENTS HERE --------------------
choose_pricelist = timokatalogos.lista_2020[-1]
# for choose_pricelist in timokatalogos.lista_2020:
from_date = choose_pricelist.start
to_date = choose_pricelist.end
id = choose_pricelist.id
dates_ranges = pd.date_range(from_date, to_date)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{id}.xlsx'

# -------------------- TAKE TIMESTAMP --------------------
start_timestamp = dt.now().strftime('%d-%m %H:%M:%S')

# -------------------- ADD COUNTERS FOR SUCCESS DIFFERENCES --------------------
found_changes_counter = 0
tries = 0

while True:
    tries += 1
    # -------------------- ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    print('<---------------------------------->')
    print(f'{dt.now().strftime("%d-%m %H:%M:%S")} :ΈΝΑΡΞΗ ΑΝΑΖΗΤΗΣΗΣ: {tries}')

    # -------------------- ΔΙΑΒΑΖΩ ΤΗΝ ΤΙΜΗ ΤΖΙΡΟΥ ΑΠΟ ΤΟ TXT --------------------
    with open('tziros.txt', 'r') as file:
        tziros = float(file.read())

    # -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ SQL DB --------------------
    timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

    # -------------------- READ SALES SQL DB --------------------
    sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                              sql_connect.sql_cnx())

    # -------------------- MERGE RESULTS PANDAS--------------------
    final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
        by=['SalesQuantity'])

    # -------------------- GROUP BY BRANDS TO SLACK --------------------
    brand_sales = final_result[['BRAND', 'SalesQuantity', 'Turnover']].groupby(by='BRAND').sum() \
        .sort_values('Turnover').reset_index()

    # -------------------- ΕΝΑΡΞΗ ΕΛΕΓΧΟΥ --------------------
    if tziros != round(final_result.Turnover.sum(), 2):

        # -------------------- READ SALES QUANTITY AND TurnOver PER DAY PER SQL DB --------------------
        quantity_per_day = []
        tziros_per_day = []
        for specific_date in dates_ranges:
            sales_per_day = pd.read_sql_query(
                sql_select.get_sales_for_every_day(specific_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                sql_connect.sql_cnx())
            quantity_per_day.append(sales_per_day.SalesQuantity.sum())
            tziros_per_day.append(round(sales_per_day.Turnover.sum(), 2))

        # -------------------- ADD +=1 TO THE COUNTER --------------------
        found_changes_counter += 1

        # ------------- OPEN FILE | WRITE ----------------------------
        excel_export.export(path_to_file, final_result)

        # -------------------- PLOT --------------------
        plt.figure(figsize=(16, 8), dpi=150)
        plt.subplot(2, 1, 1,
                    title=f'ΕΝΕΡΓΕΙΑ: {id}η || {choose_pricelist.comments} || [ΕΝΑΡΞΗ: {from_date.strftime("%d-%m")} - ΛΗΞΗ: {to_date.strftime("%d-%m")}]')
        plt.bar(brand_sales.BRAND, brand_sales.Turnover, alpha=0.5, color='red', label='ΤΖΙΡΟΣ')
        plt.plot(brand_sales.BRAND, brand_sales.SalesQuantity, alpha=0.5, color='blue', label='ΠΟΣΟΤΗΤΑ', marker='o',
                 linestyle="None")
        for x, y in zip(brand_sales.BRAND, brand_sales.SalesQuantity):
            if y - int(y) == 0:
                quant_type = 'TEM'
            else:
                quant_type = 'ΚΙΛ'
            label = "{:.2f} {}".format(y, quant_type)

            # this method is called for each point
            plt.annotate(label,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 2),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center
        plt.xticks(rotation=20)
        plt.grid(True, alpha=0.8)
        plt.legend()

        plt.subplot(212, xlabel=f'ΗΜΕΡΟΜΗΝΙΕΣ (EΝΗΜΕΡΩΘΗΚΕ:{dt.now().strftime("%d/%m %H:%M:%S")})',
                    title=f"""
ΠΩΛΗΣΕΙΣ ΑΝΑ ΗΜΕΡΑ || ΣΥΝΟΛΑ: {round(final_result.SalesQuantity.sum(), 2)}TEM / {round(final_result.Turnover.sum(), 2)}€  
""")
        colors = [plt.cm.Spectral(i / float(len(dates_ranges))) for i in range(len(dates_ranges))]
        plt.bar(dates_ranges.strftime('%a \n%d/%m'), tziros_per_day, alpha=0.9, color=colors, label='ΤΖΙΡΟΣ')
        plt.plot(dates_ranges.strftime('%a \n%d/%m'), quantity_per_day, alpha=0.9, color='darkgreen', label='ΠΟΣΟΤΗΤΑ',
                 marker='o',
                 linestyle="None")
        for x, y in zip(dates_ranges.strftime('%a \n%d/%m'), quantity_per_day):
            label = "{:.2f} TEM".format(y)

            # this method is called for each point
            plt.annotate(label,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center
        plt.axhline(y=round(np.mean(tziros_per_day), 2), xmin=0, xmax=1, linestyle='-.',
                    label=f'Μ.Ο. ΤΖΙΡΟΥ: ({round(np.mean(tziros_per_day), 2)} EUR)',
                    color='black', alpha=.2)
        plt.axhline(y=round(np.mean(quantity_per_day)), xmin=0, xmax=1, linestyle='--',
                    label=f'Μ.Ο. ΠΟΣΟΤΗΤΑΣ: ({round(np.mean(quantity_per_day))} TEM)',
                    color='red', alpha=.4)
        plt.grid(True, alpha=0.2)
        plt.legend()
        plt.tight_layout()
        plt.savefig('views.png')
        # plt.show()
        plt.close()

        # -------------------- TREE MAP --------------------
        # Prepare Data
        try:
            df = brand_sales

            labels = df.apply(
                lambda x: f'{x[0]}\n({x[1]} {"TEM" if x[1] - int(x[1]) == 0 else "ΚΙΛ"})\n({round(x[2], 2)} EUR)',
                axis=1)
            sizes = df['SalesQuantity'].values.tolist()
            colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]

            # Draw Plot
            plt.figure(figsize=(16, 8), dpi=150)
            squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

            # Decorate
            plt.title(
                f"ΠΩΛΗΣΕΙΣ ΠΟΣΟΤΗΤΑ || ΣΥΝΟΛΑ: {round(final_result.SalesQuantity.sum(), 2)}TEM / {round(final_result.Turnover.sum(), 2)}€  ")
            plt.axis('off')
            plt.savefig('tree_map_quantity.png')
            # plt.show()
            plt.close()
        except ZeroDivisionError:
            print('ΣΦΑΛΜΑ ZeroDivisionError ΣΤΟ TREE MAP')
        except:
            print('ΑΛΛΟ ΣΦΑΛΜΑ ΣΤΟ TREE MAP')
        finally:
            plt.close()

        # -------------------- READ VERSION OF PRICELIST IN TXT --------------------
        with open('version.txt', 'r') as file:
            version = int(file.read())

        # -------------------- CHECK IF WE GOT NEW VERSION --------------------
        if version == id:

            # -------------------- SLACK BOT DELETE (4 OLD POSTS) --------------------
            x = (slack_app.history(slack_app.channels_id[0]))
            for i in range(4):
                timer = (x['messages'][i]['ts'])
                slack_app.delete(slack_app.channels_id[0], timer)
        else:

            # -------------------- FILE WRITE NEW ID --------------------
            with open('version.txt', 'w') as file:
                file.write(f'{id}')

        choose_pricelist.quantity = round(final_result.SalesQuantity.sum(), 2)
        choose_pricelist.turn_over = round(final_result.Turnover.sum(), 2)

        # -------------------- SLACK BOT ADD TEXT --------------------
        report = f"""
        >ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
        ΠΟΡΕΙΑ ΠΩΛΗΣΕΩΝ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ:
        ` ΣΥΜΜΕΤΕΧΟΥΝ: \t {len(final_result)} ΠΡΟΪΟΝΤΑ `
        ` DATERANGE: \t ΑΠΟ: {from_date.strftime("%d-%m-%Y")} \t ΕΩΣ: {to_date.strftime("%d-%m-%Y")} `
        ` ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ: \t {round(final_result.SalesQuantity.sum(), 2)} TEM `
        ` M.O. / ΗΜΕΡΑ : \t {round(np.mean(quantity_per_day))} TEM ` 
        ` ΤΖΙΡΟΣ ΠΩΛΗΣΕΩΝ: \t {round(final_result.Turnover.sum(), 2)} EUR `
        ` M.O. / ΗΜΕΡΑ : \t {round(np.mean(tziros_per_day), 2)} EUR `
        ` Α/Α ΕΝΕΡΓΕΙΑ: {choose_pricelist.id}`
        ` {choose_pricelist.comments}`
        ```{brand_sales}```
        """

        slack_app.send_text(report, slack_app.channels[0])

        # -------------------- SLACK BOT ADD FILES --------------------
        slack_app.send_files(f'{id}.xlsx', path_to_file, 'xlsx', slack_app.channels[0])
        slack_app.send_files('views.png', 'views.png', 'png', slack_app.channels[0])
        slack_app.send_files('tree_map_quantity.png', 'tree_map_quantity.png', 'png', slack_app.channels[0])
    else:

        # -------------------- ΕΚΤΥΠΩΝΩ STATEMENT --------------------
        print(f'{dt.now().strftime("%d-%m %H:%M:%S")} :NOTHING TO REPORT:')

    # -------------------- WRITE TZIROS ON TXT --------------------
    with open('tziros.txt', 'w') as file:
        file.write(f'{round(final_result.Turnover.sum(), 2)}')

    # -------------------- ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    print(f'{start_timestamp} :ΑΛΛΑΓΕΣ: {found_changes_counter}')

    # -------------------- ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    print(f'{dt.now().strftime("%d-%m %H:%M:%S")} :5 MINUTES PAUSE')

    # -------------------- ADD SLEEP TIMER --------------------
    time.sleep(300)  # 5 minutes
