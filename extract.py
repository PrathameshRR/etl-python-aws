# Libraries needed for the tutorial

import pandas as pd
import requests
import io

# Downloading the NYT csv file from GitHub

urlNYT = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"  # Make sure the url is the raw version of the file on GitHub
downloadNYT = requests.get(urlNYT).content

# Downloading the John Hopkins csv file from GitHub

urlJH = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"  # Make sure the url is the raw version of the file on GitHub
downloadJH = requests.get(urlJH).content

# Reading the downloaded content and turning it into a pandas dataframe
dfNYT = pd.read_csv(io.StringIO(downloadNYT.decode('utf-8')),index_col=0, parse_dates=True)

dfJH = pd.read_csv(io.StringIO(downloadJH.decode('utf-8')),index_col=0, parse_dates=True)
# Printing out the first 5 rows of the dataframe
# print(df)

dfNYT.info()
dfJH.info()