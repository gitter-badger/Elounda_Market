#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app
# channel 1 is ενημερώσεις


def run(id):
    x = (slack_app.history(slack_app.channels_id[id]))
    for i in range(len(x['messages'])):
        percent = int((100 * (i + 1)) / len(x['messages']))
        filler = "█" * (percent // 2)
        remaining = '-' * ((100 - percent) // 2)
        timer = (x['messages'][i]['ts'])
        slack_app.delete(slack_app.channels_id[id], timer)
        print(f'\r:slack: SLACK DELETE ALL ENTRIES DONE:[{filler}{remaining}]{percent}%', end='', flush=True)
    print()


# get list of slack channels order
print(slack_app.channels)
