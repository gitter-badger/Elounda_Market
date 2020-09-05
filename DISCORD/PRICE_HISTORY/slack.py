#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(forma_id):
    slack_app.send_text(f"""
>:python: : ΕΚΤΑΚΤΟ ΔΗΜΟΣΙΕΥΜΑ
>ΔΗΜΙΟΥΡΓΗΘΗΚΕ ΑΡΧΕΙΟ ΤΙΜΩΝ ΓΙΑ ΤΟ ΠΑΡΑΣΑΤΙΚΟ: {forma_id}
>:fbwow:
    """, slack_app.channels[6])
