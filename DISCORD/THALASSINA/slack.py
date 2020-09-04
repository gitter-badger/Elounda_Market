#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def send(file_path):
    slack_app.send_text("""
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Θαλασσινά.xlsx
>:java:
>Data Science Tools Used:
>:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow: 
    """, slack_app.channels[1])

    slack_app.send_files('Θαλασσινά.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('sea_views.png', 'images/sea_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('thalassina_tree_map.png', 'images/thalassina_tree_map.png', 'png', slack_app.channels[1])