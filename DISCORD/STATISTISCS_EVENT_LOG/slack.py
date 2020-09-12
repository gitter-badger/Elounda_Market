#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(data):
    slack_app.send_text(f"""
>:python: : ΣΤΑΤΙΣΤΙΚΟ ΔΗΜΟΣΙΕΥΜΑ
> ΕΤΗΣΙΑ ΚΑΤΑΜΕΤΡΗΣΗ ΕΙΔΩΝ ΠΟΥ ΔΕΝ ΑΝΑΓΝΩΡΙΣΤΗΚΑΝ ΣΤΟ ΤΑΜΕΙΟ ΑΠΟ ΤΑ SCANNER
>:fbwow:
    """, slack_app.channels[7])
    slack_app.send_files('no_item_found.png', 'images/no_item_found.png', 'png', slack_app.channels[7])

