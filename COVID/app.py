#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from COVID import plot, slack
from DISCORD.DELETE import delete_slack_chat
import pandas as pd
import requests


# MAKE DF Reports Viewable
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# -------------------- DATAFRAME FUNCTION --------------------
def prepare_dataframe():
    url = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
    r = requests.get(url)
    with open('covid_data.csv', 'wb') as f:
        f.write(r.content)
    df =pd.read_csv('covid_data.csv')
    return df


# -------------------- DATAFRAME --------------------
covid_data = prepare_dataframe()
print(covid_data)

# -------------------- GET ALL COUNTRIES --------------------
countries = covid_data.location.unique()
print(countries)

# -------------------- SELECT WORLD --------------------
covid_data_world = covid_data[covid_data.location == 'World']
print(covid_data_world.new_deaths.sum())

# -------------------- SELECT GREECE --------------------
covid_data_greece = covid_data[covid_data['location'] == 'Greece']
# -------------------- SELECT ITALY --------------------
covid_data_italy = covid_data[covid_data.location == 'Italy']

# -------------------- PLOT GREECE --------------------
plot.plot_greece_graph(covid_data_greece, covid_data_italy)

# -------------------- SLACK --------------------
delete_slack_chat.run(8)
slack.run()
