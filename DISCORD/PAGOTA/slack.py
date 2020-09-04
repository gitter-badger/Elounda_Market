#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(file_path):
    slack_app.send_text("""
>:slack:
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Παγωτά.xlsx
>:java: :python: :fbwow:
    """, slack_app.channels[1])

    slack_app.send_files('Παγωτά.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('pagota_views.png', 'images/pagota_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('pagota_tree_map.png', 'images/pagota_tree_map.png', 'png', slack_app.channels[1])
