#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(file_path):
    slack_app.send_text("""
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ενημερώθηκε Το Αρχείο: Κερούλης.xlsx
>:java:
>Data Science Tools Used:
>:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow: 
    """, slack_app.channels[1])

    slack_app.send_files('Κερούλης.xlsx', file_path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('keroulis_views.png', 'images/keroulis_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('keroulis_tree_map.png', 'images/keroulis_tree_map.png', 'png', slack_app.channels[1])
