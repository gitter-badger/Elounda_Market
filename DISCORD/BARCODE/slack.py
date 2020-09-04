#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app

def app(sql_answer):
    slack_app.send_text(f"""
>:python: : ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>ΕΛΕΓΧΟΣ ΓΙΑ ΔΙΠΛΑ BARCODES 
```{sql_answer}```
>:fbwow:
    """, slack_app.channels[1])