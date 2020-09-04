#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app


def app(path):
    slack_app.send_text("""
>:slack:
>ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>ΣΤΑΤΙΣΤΙΚΑ_ΧΡΗΣΗΣ_PDA
>Ενημερώθηκε Το Αρχείο: sql.xlsx
>:java: :python: :fbwow:
    """, slack_app.channels[1])
    slack_app.send_files('sql.xlsx', path, 'xlsx', slack_app.channels[1])
    slack_app.send_files('pda_views.png', 'images/pda_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('pda_tree_map.png', 'images/pda_tree_map.png', 'png', slack_app.channels[1])
