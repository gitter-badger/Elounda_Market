#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(order_id, output_file, path_to_file, cost, elounda_sales, kerdos_elounda, bazaar_sales, kerdos_bazaar):
    slack_output_text = f"""
> :python: : ΕΒΔΟΜΑΔΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
> ΚΑΤΑΧΩΡΗΘΗΚΑΝ ΤΑ ΤΙΜΟΛΟΓΙΑ: {order_id}
> ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {cost} EUR
> ΤΑΜΕΙΟ ΠΩΛΗΣΗ ELOUNDA: {elounda_sales} EUR \t ΚΕΡΔΟΣ: {kerdos_elounda} EUR
> ΤΑΜΕΙΟ ΠΩΛΗΣΗ BAZAAR :{bazaar_sales} EUR  \t ΚΕΡΔΟΣ: {kerdos_bazaar} EUR
>:fbwow: 
    """
    slack_app.send_text(slack_output_text, slack_app.channels[5])
    slack_app.send_files(output_file, path_to_file, 'xlsx', slack_app.channels[5])
    slack_app.send_files('bazaar_views.png', 'images/bazaar_views.png', 'png', slack_app.channels[5])
    slack_app.send_files('markup_bazaar_views.png', 'images/markup_bazaar_views.png', 'png', slack_app.channels[5])
    slack_app.send_files('retail_to_retail.png', 'images/retail_to_retail.png', 'png', slack_app.channels[5])
