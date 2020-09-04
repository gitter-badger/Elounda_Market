#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(supplier, katastima, final_result, get_year, detailed, detailed_file_path):
    slack_app.send_text(f"""
>:python: : ΕΚΤΑΚΤΟ ΔΗΜΟΣΙΕΥΜΑ
>ΠΡΟΜΗΘΕΥΤΗΣ:\t{supplier}
>ΥΠΟΚΑΤΑΣΤΗΜΑ:\t{katastima()}
>ΠΡΟΪΟΝΤΑ:\t{len(final_result)}
>ΣΥΝΟΛΙΚΗ ΠΟΣΟΤΗΤΑ:\t{sum(final_result['Ποσότητα'])} ΤΕΜ
>ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ:\t{round(final_result['SUM'].sum(), 2)} €
>ΕΤΟΣ ΑΝΑΖΗΤΗΣΗΣ ΚΟΣΤΟΥΣ:\t{get_year}
>:fbwow: 
    """, slack_app.channels[6])

    # ----------------SLACK BOT FILES----------------------------
    slack_app.send_files(detailed, detailed_file_path, 'xlsx', slack_app.channels[6])
