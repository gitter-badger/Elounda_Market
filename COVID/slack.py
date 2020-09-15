#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app


def run():
    slack_output_text = f"""
> :python: : ΕΚΤΑΚΤΟ ΔΗΜΟΣΙΕΥΜΑ
> COVID GRAPH GREECE
>:fbwow: 
    """
    slack_app.send_text(slack_output_text, slack_app.channels[8])
    slack_app.send_files('greece_deaths.png', 'images/greece_deaths.png', 'png', slack_app.channels[8])