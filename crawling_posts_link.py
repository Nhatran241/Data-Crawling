import pandas as pd
import requests

sitemaps = pd.read_csv('post.csv')

with open('post-final.csv', 'a') as f:
    for index,sitemap in sitemaps.iterrows():
        url = sitemap[2]
        if pd.notna(url):
            if  ".txt" in url:
                print(url)
                r = requests.get(url, allow_redirects=True)
                f.write('\n')
                df = pd.DataFrame({"title": sitemap[1], "content": r.content}, index=[index])
                df.to_csv('post-final.csv', index=True, header=False, mode='a')
