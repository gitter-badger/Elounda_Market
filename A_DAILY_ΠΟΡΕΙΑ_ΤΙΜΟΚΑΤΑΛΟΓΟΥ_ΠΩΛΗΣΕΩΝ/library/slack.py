#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app
import numpy as np


def run(final_result, from_date, to_date, quantity_per_day,
        tziros_per_day, choose_pricelist, brand_sales, path_to_file, tim_id):
    report = f"""
>:python: : ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ : :fbwow:
>ΠΟΡΕΙΑ ΠΩΛΗΣΕΩΝ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ:
>ΣΥΜΜΕΤΕΧΟΥΝ: \t {len(final_result)} ΠΡΟΪΟΝΤΑ 
>DATERANGE: \t ΑΠΟ: {from_date.strftime("%d-%m-%Y")} \t ΕΩΣ: {to_date.strftime("%d-%m-%Y")} 
>ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ: \t {round(final_result.SalesQuantity.sum(), 2)} TEM 
> M.O. / ΗΜΕΡΑ : \t {round(np.mean(quantity_per_day))} TEM 
> ΤΖΙΡΟΣ ΠΩΛΗΣΕΩΝ: \t {round(final_result.Turnover.sum(), 2)} EUR 
> M.O. / ΗΜΕΡΑ : \t {round(np.mean(tziros_per_day), 2)} EUR 
> Α/Α ΕΝΕΡΓΕΙΑ: {choose_pricelist.tim_id}
> {choose_pricelist.comments}
```{brand_sales}``` 
            """

    slack_app.send_text(report, slack_app.channels[0])

    # -------------------- SLACK BOT ADD FILES --------------------
    slack_app.send_files(f'{tim_id}.xlsx', path_to_file, 'xlsx', slack_app.channels[0])
    slack_app.send_files('bar.png', 'images/bar.png', 'png', slack_app.channels[0])
    slack_app.send_files('daily.png', 'images/daily.png', 'png', slack_app.channels[0])
    slack_app.send_files('tree_map_quantity.png', 'images/tree_map_quantity.png', 'png', slack_app.channels[0])
    slack_app.send_files('pricelist_pie.png', 'images/pricelist_pie.png', 'png', slack_app.channels[0])
    slack_app.send_files('heatmap.png', 'images/heatmap.png', 'png', slack_app.channels[0])
    slack_app.send_files('heatmap_turnover.png', 'images/heatmap_turnover.png', 'png', slack_app.channels[0])
    slack_app.send_files('boxplot.png', 'images/boxplot.png', 'png', slack_app.channels[0])
    slack_app.send_files('violin.png', 'images/violin.png', 'png', slack_app.channels[0])


