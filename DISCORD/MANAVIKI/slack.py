#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(file_path):
    slack_app.send_text("""
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Μαναβική.xlsx
>:java:
>Data Science Tools Used:
>:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow: 
    """, slack_app.channels[1])

    slack_app.send_files('Μαναβική.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('manaviki_views.png', 'images/manaviki_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('manaviki_tree_map.png', 'images/manaviki_tree_map.png', 'png', slack_app.channels[1])
