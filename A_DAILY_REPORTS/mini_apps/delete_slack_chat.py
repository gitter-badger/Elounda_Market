#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import slack_app
# channel is ενημερώσεις
x = (slack_app.history(slack_app.channels_id[1]))

for i in range(len(x['messages'])):
    percent = int((100 * (i + 1)) / len(x['messages']))
    filler = "█" * (percent // 2)
    remaining = '-' * ((100 - percent) // 2)
    timer = (x['messages'][i]['ts'])
    slack_app.delete(slack_app.channels_id[1], timer)
    print(f'\rSLACK DELETE ALL ENTRIES DONE:[{filler}{remaining}]{percent}%',end='', flush=True)
print()


