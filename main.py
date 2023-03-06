import pandas as pd
import os
import bar_chart_race as bcr
import numpy as np
from matplotlib import pyplot as plt
# import seaborn as sns
from matplotlib.animation import FuncAnimation

def get_data():
    path = os.getcwd()
    print(os.path.join(path, 'API_SP.POP.TOTL_DS2_en_csv_v2_4902028.csv'))
    df = pd.read_csv(os.path.join(path, 'API_SP.POP.TOTL_DS2_en_csv_v2_4902028.csv'), header=2)
    del df[df.columns[-1]]
    df_meta = pd.read_csv(os.path.join(path, 'Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_4902028.csv'))
    df_meta.dropna(subset=['Region'])
    # print(df_meta)
    # print(list(df_meta['Country Code']))
    df1 = df[df['Country Code'].isin(list(df_meta[df_meta['Region'].notna()]['Country Code']))].sort_values('1960',ascending = False).head(5)
    yrs = []
    for i in range(1960, 2021):
        yrs.append(str(i))
    df1 = df1[['Country Code'] + yrs]
    df1.set_index('Country Code', inplace=True)
    df1 = df1.transpose()
    return df1

df = get_data()
bcr.bar_chart_race(df, filename=None, figsize=(3.5,3), title='u;hy;k')