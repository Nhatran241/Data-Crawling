import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# driver = webdriver.Chrome("chromedriver.exe")

driver = webdriver.Chrome(options=options)
sitemaps = pd.read_csv('linkpost4.csv')
with open('post.csv', 'a') as f:
    for index,sitemap in sitemaps.iterrows():
        url = sitemap['link']
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        tagA = soup.find_all('a')
        title = soup.find('h1',{'class': 'page-title'})
        linkScript = ''
        postTitle = title.getText()
        for a in tagA:
            if a.getText().find('Download') != -1:
                linkScript = a.get('href')

        f.write('\n')
        df = pd.DataFrame({"title": postTitle, "download": linkScript}, index=[index])
        df.to_csv('post.csv', index=True, header=False, mode='a')


