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

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :READING SQL PRICELIST:')

    # -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ SQL DB--------------------
    timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :READING SQL SALES:')

    # -------------------- READ SALES SQL DB--------------------
    sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                              sql_connect.sql_cnx())

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :MERGING RESULTS:')

    # -------------------- MERGE RESULTS PANDAS--------------------
    final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
        by=['SalesQuantity'])

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :GROUPING RESULTS:')

    # --------------------GROUP BY BRANDS TO SLACK --------------------
    brand_sales = final_result[['BRAND', 'SalesQuantity', 'Turnover']].groupby(by='BRAND').sum() \
        .sort_values('BRAND').reset_index()

    # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
    # print(f'{dt.now()} :CHECKING DIFFERENCES:')

    # --------------------ΕΝΑΡΞΗ ΕΛΕΓΧΟΥ --------------------
    if tziros != round(final_result.Turnover.sum(), 2):

        # -------------------- ADD +=1 TO THE COUNTER --------------------
        found_changes_counter += 1

        # --------------------ΕΚΤΥΠΩΝΩ STATEMENT --------------------
        # print(f'{dt.now()} :FOUND NEW RECORDS:')

        # -------------OPEN FILE | WRITE ----------------------------
        excel_export.export(path_to_file, final_result)

        # -------------------- PLOT --------------------
        plt.figure(figsize=(15, 9))
        plt.subplot(xlabel=f'Brand (EΝΗΜΕΡΩΘΗΚΕ:{dt.now().strftime("%d/%m %H:%M:%S")})',
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
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center
        plt.grid(True, alpha=0.8)
        plt.legend()
        plt.savefig('views.png')
        plt.show()

        # -------------------- SLACK BOT DELETE (3 OLD POSTS) --------------------
        x = (slack_app.history(slack_app.channels_id[0]))
        for i in range(3):
            timer = (x['messages'][i]['ts'])
            slack_app.delete(slack_app.channels_id[0], timer)

        # -------------------- SLACK BOT ADD TEXT --------------------
        report = f"""
        >ΠΟΡΕΙΑ ΠΩΛΗΣΕΩΝ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ:
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
