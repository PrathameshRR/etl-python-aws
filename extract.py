# Libraries needed for the tutorial

import pandas as pd
import requests
import io

# Downloading the NYT csv file from GitHub

nyt_csv_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"  # Make sure the url is the raw version of the file on GitHub
download_nyt_data = requests.get(nyt_csv_url).content

# Downloading the John Hopkins csv file from GitHub

jh_csv_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"  # Make sure the url is the raw version of the file on GitHub
download_jh_data = requests.get(jh_csv_url).content

# Reading the downloaded content and turning it into a pandas dataframe
data_frame_nyt = pd.read_csv(io.StringIO(download_nyt_data.decode('utf-8')))

data_frame_jh = pd.read_csv(io.StringIO(download_jh_data.decode('utf-8')))
# Printing out the first 5 rows of the dataframe
# print(df)`

# print(data_frame_nyt.head())
# print(data_frame_jh.head())

##print(data_frame_jh["Country/Region" == "US"])

#us_data_jh_almost_final = data_frame_jh[data_frame_jh["Country/Region"] == "US"]

#us_data_jh_final = us_data_jh_almost_final.loc['Date', 'Recovered']
# us_data_jh_final = us_data_jh_almost_final.drop(['Confirmed', 'Deaths', 'Province/State','Country/Region'], inplace=True, axis=1)
data_frame_jh.columns = ['Date','Country', 'State', 'Confirmed', 'Recovered', 'Deaths']
data_frame_nyt.columns = ['Date','Cases','Deaths']

df = data_frame_jh[data_frame_jh.Country == "US"]

dff = df.loc[:,['Date','Recovered']]

Inner_Join = pd.merge(dff,data_frame_nyt, how='inner', on=['Date', 'Date'])
print(Inner_Join)


#print(dff)
