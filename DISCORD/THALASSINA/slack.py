#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def send(file_path):
    slack_app.send_text("""
>:python: : ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Θαλασσινά.xlsx
>:fbwow:
    """, slack_app.channels[1])

    slack_app.send_files('Θαλασσινά.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('sea_views.png', 'images/sea_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('thalassina_tree_map.png', 'images/thalassina_tree_map.png', 'png', slack_app.channels[1])