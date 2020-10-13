#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import slack_app

def run(output_file):
    slack_app.send_text("""
>:python: : ΗΜΕΡΗΣΙΟ ΔΗΜΟΣΙΕΥΜΑ
>ΣΤΑΤΙΣΤΙΚΑ ELOUNDA MARKET
>:fbwow:
    """, slack_app.channels[1])

    slack_app.send_files('views.png', 'images/views.png', 'png', slack_app.channels[1])
    slack_app.send_files('heatmap.png', 'images/heatmap.png', 'png', slack_app.channels[1])
    slack_app.send_files('box.png', 'images/box.png', 'png', slack_app.channels[1])


def kat_run(data, brand):
    slack_app.send_text(f"""
    >:python: : {brand} : :fbwow:
    ```{data}```
        """, slack_app.channels[1])
    slack_app.send_files('kataskevastis_views.png', 'images/kataskevastis_views.png', 'png', slack_app.channels[1])
    slack_app.send_files('heatmap.png', 'images/heatmap.png', 'png', slack_app.channels[1])