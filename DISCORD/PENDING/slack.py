#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app


def run(output_file, path_to_file):
    slack_app.send_text("""
>:python: : ΜΗΝΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
>Ολοκληρώθηκε η εξαγωγή εκκρεμοτήτων για έως σήμερα:
>:fbwow:
    """, slack_app.channels[4])
    slack_app.send_files(output_file, path_to_file, 'xlsx', slack_app.channels[4])

