from urllib.request import urlopen
from bs4 import BeautifulSoup

url ='https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')

today_kospi = soup.find_all('div',attrs={'class':'lft'})

res = [span.string for span in today_kospi]


print('{}에 코스피지수는{}'.format(soup.select('#time3')[0].text,soup.select('#KOSPI_now')[0].text))
