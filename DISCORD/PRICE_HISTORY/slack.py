#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app


def run(forma_id):
    slack_app.send_text(f"""
>:python: : ΕΚΤΑΚΤΟ ΔΗΜΟΣΙΕΥΜΑ
>ΔΗΜΙΟΥΡΓΗΘΗΚΕ ΑΡΧΕΙΟ ΤΙΜΩΝ ΓΙΑ ΤΟ ΠΑΡΑΣΑΤΙΚΟ: {forma_id}
>ΤΑ ΑΡΧΕΙΑ ΕΙΝΑΙ ΔΙΑΘΕΣΙΜΑ ΣΤΟΝ ΦΑΚΕΛΟ OneDrive/SUPPLIER_CHECK/history/{forma_id}/....png  
>:fbwow:
    """, slack_app.channels[6])
