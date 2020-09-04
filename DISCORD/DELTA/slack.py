#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(file_path):
    slack_app.send_text("""
>:slack:
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Φρέσκο Γάλα Δέλτα POS.xlsx
>:java: :python: :fbwow:
    """, slack_app.channels[1])

    slack_app.send_files('Φρέσκο Γάλα Δέλτα POS.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('fresco_gala_delta_views.png', 'images/fresco_gala_delta_views.png', 'png',
                         slack_app.channels[1])
