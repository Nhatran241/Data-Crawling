import pandas as pd
import requests
from time import sleep
import ast
import base64
sitemaps = pd.read_csv('post-final.csv')

with open('post-final2.csv', 'a') as f:
    for index,sitemap in sitemaps.iterrows():
        code = str(sitemap[2])
        print(code.encode().decode('unicode-escape')[2:-1])
        f.write('\n')
        df = pd.DataFrame({"title": sitemap[1], "code":code.encode().decode('unicode-escape')[2:-1]}, index=[index])
        df.to_csv('post-final2.csv', index=True, header=False, mode='a')
