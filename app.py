import requests
import pandas as pd
import numpy as np

url = 'https://sscn.bkn.go.id/public/data_noexist/pendaftar_dashboard_prod.js?_=1537378604051'
a = requests.get(url, verify = False)
df = pd.DataFrame(a.json().get('data'))
df.to_csv('cpns_all.csv');

def Sosiologi(data):
    if "SOSIOLOGI" in data:
        return "TRUE"
    else:
        return np.NaN

df['YN'] = df.apply(lambda x: Sosiologi(x['PENDIDIKAN_NM']), axis=1)
df.dropna(inplace=True)
df.to_csv('cpns_sosiologi.csv')

