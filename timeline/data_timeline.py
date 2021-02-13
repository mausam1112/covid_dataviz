# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:10:03 2020

@author: Admin
"""
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd

''' Remove last two entries in this data frame '''
df = pd.read_json('data_history_oct_2.json')
df = df[56:-2]
df['active'] = df['totalCases']-df['totalRecoveries']-df['totalDeaths']

plt.style.use('seaborn')

plt.figure(figsize=(15,8))

plt.plot_date(df['date'],df['totalCases'],linestyle='solid',fmt='-', c='red',marker='o',markersize=2, label='Total Cases')
plt.plot_date(df['date'],df['totalRecoveries'],linestyle='solid',fmt='-', c='blue',marker='o',markersize=2, label='Total Recoveries')
plt.plot_date(df['date'],df['totalDeaths'],linestyle='solid',fmt='-', c='black',marker='o',markersize=2, label='Total Deaths')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.xlabel('Time')
plt.ylabel('Number of cases')
plt.tight_layout()
plt.legend()
plt.show()



