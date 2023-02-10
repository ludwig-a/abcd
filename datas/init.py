from lib import addLibraries

file = 'datas/EUR=X.csv'

data = addLibraries.pd.read_csv(file)

# to transform Date type
data.Date = addLibraries.pd.to_datetime(data.Date)

# to set the Date column rather as the index
data = data.set_index('Date')

#data.info()
