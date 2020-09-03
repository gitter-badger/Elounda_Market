#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app

def run(output_file):
    slack_app.send_text("""
    >ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
    >ΣΤΑΤΙΣΤΙΚΑ ELOUNDA MARKET
    `Ενημερώθηκε Το Αρχείο: EM.xlsx`
    >
    >Data Science Tools Used:
    >:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow: 
    """, slack_app.channels[1])

    slack_app.send_files('EM.xlsx', output_file, 'xlsx', slack_app.channels[1])
    slack_app.send_files('views.png', 'images/views.png', 'png', slack_app.channels[1])
    slack_app.send_files('kataskevastis_views.png', 'images/kataskevastis_views.png', 'png', slack_app.channels[1])

    print(' 22: SLACK DONE ')

