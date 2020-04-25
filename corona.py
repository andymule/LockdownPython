import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def makeDataframe():
    df = pd.read_csv('download.csv')
    data = pd.DataFrame()
    print(data)
    globalcases = 0
    globaldeaths = 0
    for index, c in df.iterrows():
        name = c['countriesAndTerritories']
        if name not in data.values:
            data = data.append({'name':name, 'cases':0, 'deaths':0, 'ratio':0}, ignore_index=True)
        dex = list(np.where(data["name"] == name)[0])[0]
        data.at[dex, 'cases'] += c['cases']
        data.at[dex, 'deaths'] += c['deaths']
        globalcases += c['cases']
        globaldeaths += c['deaths']
    globalratio = globalcases / globaldeaths
    print(globalratio)
    for i, row in data.iterrows():
        if row['deaths'] > 0:
            data.at[i,'ratio'] = round(row['cases']/row['deaths'], 2)
    data.to_csv('export_dataframe.csv', index = False, header=True)

# 14.2
# makeDataframe()
df = pd.read_csv('export_dataframe.csv')
subframe = pd.DataFrame(df[df['cases']>10000])
subframe = subframe.sort_values('ratio')

sns.relplot(x="ratio", y="name", size="deaths", sizes=(5, 200), data=subframe, legend=False)
sns.lineplot(x=[14.2, 14.2, 14.2], y=[0,10,27], sizes=(5,10), size=10, legend=False)
plt.show()
