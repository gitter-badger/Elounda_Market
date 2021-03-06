#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ.library import sql_select, timokatalogos, excel_export, plot, slack
from Private import sql_connect, slack_app
import time
from datetime import datetime as dt
import sys


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
tim_id = choose_pricelist.tim_id
dates_ranges = pd.date_range(from_date, to_date)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{tim_id}.xlsx'

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
    timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.connect())
    barcodes = tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)

    # -------------------- READ SALES SQL DB --------------------
    sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                              sql_connect.connect())

    # -------------------- MERGE RESULTS PANDAS--------------------
    final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
        by=['SalesQuantity'])

    # -------------------- GROUP BY BRANDS TO SLACK --------------------
    brand_sales = final_result[['BRAND', 'SalesQuantity', 'Turnover']].groupby(by='BRAND').sum() \
        .sort_values('Turnover').reset_index()

    # -------------------- ΕΝΑΡΞΗ ΕΛΕΓΧΟΥ --------------------
    if tziros != round(final_result.Turnover.sum(), 2):

        # -------------------- GET RICH DETAILS  --------------------

        date = [i.strftime('%Y-%m-%d') for i in dates_ranges]

        rich_details = pd.read_sql_query(sql_select.get_rich_details(tuple(date), barcodes), sql_connect.connect())

        sales_pivot = rich_details.pivot_table(index='BRAND', columns='DATE', values='QUANTITY')
        sales_pivot = sales_pivot.fillna(0)

        turnover_pivot = rich_details.pivot_table(index='BRAND', columns='DATE', values='TURNOVER')
        turnover_pivot = turnover_pivot.fillna(0)

        plot.heatmap(sales_pivot, '(SEABORN HEAT MAP) / ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ')
        plot.heatmap_02(turnover_pivot, '(SEABORN HEAT MAP) / TΖΙΡΟΣ ΠΩΛΗΣΕΩΝ')
        plot.sea_boxplot(rich_details, '(SEABORN BOX PLOT) / ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ')
        plot.sea_violinplot(rich_details, '(SEABORN VIOLIN PLOT) / TΖΙΡΟΣ ΠΩΛΗΣΕΩΝ')

        # -------------------- READ SALES QUANTITY AND TurnOver PER DAY PER SQL DB --------------------
        quantity_per_day = []
        tziros_per_day = []
        for specific_date in dates_ranges:
            sales_per_day = pd.read_sql_query(
                sql_select.get_sales_for_every_day(specific_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                sql_connect.connect())
            quantity_per_day.append(sales_per_day.SalesQuantity.sum())
            tziros_per_day.append(round(sales_per_day.Turnover.sum(), 2))

        # -------------------- ADD +=1 TO THE COUNTER --------------------
        found_changes_counter += 1

        # ------------- OPEN FILE | WRITE ----------------------------
        excel_export.export(path_to_file, final_result)

        # -------------------- PLOT --------------------
        plot.run(choose_pricelist, from_date, to_date, brand_sales, final_result, dates_ranges,
                 tziros_per_day, quantity_per_day, tim_id)

        # -------------------- READ VERSION OF PRICELIST IN TXT --------------------
        with open('version.txt', 'r') as file:
            version = int(file.read())

        # -------------------- CHECK IF WE GOT NEW VERSION --------------------
        if version == tim_id:

            # -------------------- SLACK BOT DELETE (10 OLD POSTS) --------------------
            x = (slack_app.history(slack_app.channels_id[0]))
            for i in range(10):
                timer = (x['messages'][i]['ts'])
                slack_app.delete(slack_app.channels_id[0], timer)
        else:

            # -------------------- FILE WRITE NEW ID --------------------
            with open('version.txt', 'w') as file:
                file.write(f'{tim_id}')

        choose_pricelist.quantity = round(final_result.SalesQuantity.sum(), 2)
        choose_pricelist.turn_over = round(final_result.Turnover.sum(), 2)

        # -------------------- SLACK BOT ADD TEXT --------------------
        slack.run(final_result, from_date, to_date, quantity_per_day, tziros_per_day,
                  choose_pricelist, brand_sales, path_to_file, tim_id)
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
    try:
        time.sleep(300)  # 5 minutes
    except KeyboardInterrupt:
        print('EXIT REQUESTED BY: Ioannis E. Kommas')
        sys.exit(1)
