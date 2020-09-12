#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(data):
    slack_app.send_text(f"""
>:python: : ΣΤΑΤΙΣΤΙΚΟ ΔΗΜΟΣΙΕΥΜΑ
> ΚΑΤΑΧΩΡΗΣΕΙΣ ΝΕΩΝ ΕΙΔΩΝ ΓΙΑ ΤΟ ΤΡΕΧΩΝ ΕΤΟΣ / ΧΡΗΣΤΗ
>:fbwow:
    """, slack_app.channels[7])
    slack_app.send_files('new_items_per_user.png', 'images/new_items_per_user.png', 'png', slack_app.channels[7])

