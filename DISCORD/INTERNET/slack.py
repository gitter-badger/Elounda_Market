#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def app(ELOUNDA_MARKET, LATO_01, LATO_02):
    # ----------------SLACK BOT----------------------------
    output = f"""
>:python: : ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>ΕΛΕΓΧΟΣ INTERNET ΣΤΑ ΚΑΤΑΣΤΗΜΑΤΑ
>{ELOUNDA_MARKET}
>{LATO_01}
>{LATO_02}
>:fbwow:
    """
    slack_app.send_text(output, slack_app.channels[1])
    print('END')
