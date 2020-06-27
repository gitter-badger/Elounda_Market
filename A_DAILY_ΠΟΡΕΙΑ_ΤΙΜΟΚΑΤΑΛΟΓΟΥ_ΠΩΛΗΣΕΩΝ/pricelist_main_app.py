#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ.library import sql_select, timokatalogos, excel_export
from Private import sql_connect, slack_app
import matplotlib.pyplot as plt
import time
from _datetime import datetime as dt



# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- STATEMENTS HERE --------------------
choose = timokatalogos.lista_2020[-1]
from_date = choose.start
to_date = choose.end
id = choose.id
dates_ranges = pd.date_range(from_date, to_date)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{id}.xlsx'

# -------------------- TAKE TIMESTAMP --------------------
start_timestamp = dt.now().strftime('%d-%m %H:%M:%S')

# -------------------- ADD COUNTER FOR SUCCESS DIFFERENCES --------------------
found_changes_counter = 0

while True:

    # -------------------- ΔΙΑΒΑΖΩ ΤΗΝ ΤΙΜΗ ΤΖΙΡΟΥ ΑΠΟ ΤΟ TXT--------------------
    with open('tziros.txt', 'r') as file:
        tziros = float(file.read())

    # -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ SQL DB--------------------
    timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

    # -------------------- READ SALES SQL DB--------------------
    sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                              sql_connect.sql_cnx())

    # -------------------- MERGE RESULTS PANDAS--------------------
    final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
        by=['SalesQuantity'])

    # --------------------GROUP BY BRANDS TO SLACK --------------------
    brand_sales = final_result[['BRAND', 'SalesQuantity', 'Turnover']].groupby(by='BRAND').sum() \
        .sort_values('Turnover').reset_index()

    # --------------------ΕΝΑΡΞΗ ΕΛΕΓΧΟΥ --------------------
    if tziros != round(final_result.Turnover.sum(), 2):

        # -------------------- READ SALES QUANTITY AND TurnOver PER DAY PERSQL DB--------------------
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

        # -------------OPEN FILE | WRITE ----------------------------
        excel_export.export(path_to_file, final_result)

        # -------------------- PLOT --------------------
        plt.figure(figsize=(15, 9))
        plt.subplot(2, 1, 1,
                    title=f'ΕΝΕΡΓΕΙΑ: {id}η || {choose.comments} || [ΕΝΑΡΞΗ: {from_date.strftime("%d-%m")} - ΛΗΞΗ: {to_date.strftime("%d-%m")}]')
        plt.bar(brand_sales.BRAND, brand_sales.Turnover, alpha=0.5, color='red', label='ΤΖΙΡΟΣ')
        plt.plot(brand_sales.BRAND, brand_sales.SalesQuantity, alpha=0.5, color='blue', label='ΠΟΣΟΤΗΤΑ', marker='o',
                 linestyle="None")
        for x, y in zip(brand_sales.BRAND, brand_sales.SalesQuantity):
            label = "{:.2f} TEM".format(y)

            # this method is called for each point
            plt.annotate(label,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 2),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center
        plt.grid(True, alpha=0.8)
        plt.legend()

        plt.subplot(2, 1, 2, xlabel=f'ΗΜΕΡΟΜΗΝΙΕΣ (EΝΗΜΕΡΩΘΗΚΕ:{dt.now().strftime("%d/%m %H:%M:%S")})',
                    title=f'ΠΩΛΗΣΕΙΣ ΑΝΑ ΗΜΕΡΑ || ΣΥΝΟΛΑ: {final_result.SalesQuantity.sum()}TEM / {round(final_result.Turnover.sum(), 2)}€  ')
        plt.bar(dates_ranges.strftime('%d/%m'), tziros_per_day, alpha=0.5, color='blue', label='ΤΖΙΡΟΣ')
        plt.plot(dates_ranges.strftime('%d/%m'), quantity_per_day, alpha=0.5, color='red', label='ΠΟΣΟΤΗΤΑ', marker='o',
                 linestyle="None")
        for x, y in zip(dates_ranges.strftime('%d/%m'), quantity_per_day):
            label = "{:.2f} TEM".format(y)

            # this method is called for each point
            plt.annotate(label,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 2),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center
        plt.grid(True, alpha=0.8)
        plt.legend()

        plt.savefig('views.png')
        plt.show()

        # --------------------READ VERSION OF PRICELIST IN TXT--------------------
        with open('version.txt', 'r') as file:
            version = int(file.read())

        # -------------------- CHECK IF WE GOT NEW VERSION --------------------
        if version == id:

            # -------------------- SLACK BOT DELETE (3 OLD POSTS) --------------------
            x = (slack_app.history(slack_app.channels_id[0]))
            for i in range(3):
                timer = (x['messages'][i]['ts'])
                slack_app.delete(slack_app.channels_id[0], timer)
        else:

            # -------------------- FILE WRITE NEW ID --------------------
            with open('version.txt', 'w') as file:
                file.write(f'{id}')

        choose.quantity = final_result.SalesQuantity.sum()
        choose.turn_over = {round(final_result.Turnover.sum(), 2)}

        # -------------------- SLACK BOT ADD TEXT --------------------
        report = f"""
        >ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
        ΠΟΡΕΙΑ ΠΩΛΗΣΕΩΝ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ:
        ` ΣΥΜΜΕΤΕΧΟΥΝ: \t {len(final_result)} ΠΡΟΪΟΝΤΑ `
        ` DATERANGE: \t ΑΠΟ: {from_date.strftime("%d-%m-%Y")} \t ΕΩΣ: {to_date.strftime("%d-%m-%Y")} `
        ` ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ: \t {final_result.SalesQuantity.sum()} TEM `
        ` ΤΖΙΡΟΣ ΠΩΛΗΣΕΩΝ: \t {round(final_result.Turnover.sum(), 2)} € `
        ` Α/Α ΕΝΕΡΓΕΙΑ: {choose.id}`
        ` {choose.comments}`
        ```{brand_sales}```
        """

        slack_app.send_text(report, slack_app.channels[0])

        # -------------------- SLACK BOT ADD FILES --------------------
        slack_app.send_files(f'{id}.xlsx', path_to_file, 'xlsx', slack_app.channels[0])
        slack_app.send_files('views.png', 'views.png', 'png', slack_app.channels[0])
    else:
        pass
        # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
        # print(f'{dt.now()} :NOTHING TO REPORT:')

    # --------------------WRITE TZIROS ON TXT --------------------
    with open('tziros.txt', 'w') as file:
        file.write(f'{round(final_result.Turnover.sum(), 2)}')


    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    print(f'ΣΥΝΟΛΙΚΕΣ ΕΝΗΜΕΡΩΣΕΙΣ ΑΠΟ: {start_timestamp} : ΕΓΙΝΑΝ:{found_changes_counter}')

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    print(f'{dt.now()} :PAUSE ON: 5 MINUTES')

    # --------------------ADD SLEEP TIMER --------------------
    time.sleep(300)  # 5 minutes

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :PAUSE OFF:')
