from Private import slack_app
# channel is ενημερώσεις
x = (slack_app.history(slack_app.channels_id[1]))

for i in range(len(x['messages'])):
    timer = (x['messages'][i]['ts'])
    slack_app.delete(slack_app.channels_id[1], timer)

print('END')



