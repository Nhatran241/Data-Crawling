import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
sitemaps = pd.read_csv('sitemap.csv')
for index,sitemap in sitemaps.iterrows():
    url = sitemap['sitemap']
    urlSSL = url.replace('http','https')
    driver.get(urlSSL)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    print(content)

    linkPosts = []
    for a in soup.find_all('a'):
        linkPosts.append(a.get('href').replace('http','https'))

    df = pd.DataFrame({"link": linkPosts})
    filename = 'linkpost'+str(index)+'.csv'
    df.to_csv(filename, index=False)
