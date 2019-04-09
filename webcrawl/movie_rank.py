from selenium import webdriver
from bs4 import BeautifulSoup
ctx='../crawler/chromedriver'
driver = webdriver.Chrome(ctx)

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')
#print(soup.prettify())

movie_rank = soup.find_all('div',attrs={'class':'tit3'})

res = [div.a.string for div in movie_rank]

for i in res:
    print(i)

driver.close()