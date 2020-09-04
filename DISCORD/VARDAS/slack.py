#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app


def run(vardas):
    slack_app.send_text(vardas, slack_app.channels[4])
