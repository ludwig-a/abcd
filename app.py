from lib import addLibraries
from datas import init

addLibraries.mpf.plot(init.data['2022-01':'2022-12'], 
    figratio=(10,12),
    type='candle',
    title='EUR - 2022',
    mav=(20),
    volume=True,
    tight_layout=True,
    style='yahoo')



# Afficher la figure
addLibraries.plt.show()
