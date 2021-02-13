import pandas as pd

df_cases = pd.read_csv('\csv data\province_cases.csv')
df_active = pd.read_csv('\csv data\province_active.csv')
df_recovered = pd.read_csv('H:\mausam\python  ex\covid-19\csv data\province_recovered.csv')
df_death = pd.read_csv('\csv data\province_death.csv')

df1 = df_cases.merge(df_active, on='Province')
df2 = df1.merge(df_recovered, on='Province')
df3 = df2.merge(df_death, on='Province')
df3.to_csv('\csv data\province_data.csv')

df4 = pd.read_csv('\csv data\province_data.csv')
print(df4)
