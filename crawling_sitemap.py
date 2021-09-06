from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://robloxscripts.com/sitemap.xml")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())

sitemaps=[]
for a in soup.find_all('a'):
    if a.get('href').find('post') != -1:
        sitemaps.append(a.get('href'))

df = pd.DataFrame({"sitemap":sitemaps})
df.to_csv('sitemap.csv', index=False)