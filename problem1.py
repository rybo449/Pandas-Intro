import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import sys


pd.set_option('display.mpl_style', 'default')
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)
#plt.rcParams['figure.figsize'] = (15, 5)


df = pd.read_csv(sys.argv[1])
df['Created Date'] = pd.to_datetime(df['Created Date'], format = "%m/%d/%Y %H:%M:%S %p")
df['Created Date'] = df['Created Date'].apply(lambda x: x.strftime('%m-%d-%Y'))

fields = ['Created Date','Borough','Count']
data = df.groupby(fields[:2]).size().reset_index()


data.columns = fields
data = data.pivot(index='Created Date', columns='Borough', values='Count')
data.plot()
plt.legend(loc = 1)
plt.show()




