#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(order_id, output_file, path_to_file):
    slack_output_text = f"""
> :python: : ΕΒΔΟΜΑΔΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
> ΚΑΤΑΧΩΡΗΘΗΚΑΝ ΤΑ ΤΙΜΟΛΟΓΙΑ: {order_id}
>:fbwow: 
    """
    slack_app.send_text(slack_output_text, slack_app.channels[5])
    slack_app.send_files(output_file, path_to_file, 'xlsx', slack_app.channels[5])
    slack_app.send_files('bazaar_views.png', 'images/bazaar_views.png', 'png', slack_app.channels[5])