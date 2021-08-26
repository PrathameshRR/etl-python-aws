import pandas as pd
url = 'https://github.com/nytimes/covid-19-data/blob/master/us.csv'

print pd.read_csv(url,index_col=0,parse_dates=[0])