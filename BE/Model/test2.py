import bs4
import pandas
import requests

#urls = ['https://batdongsan321.com/nha-dat-ban/ha-noi?category=3#/','https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=2#/','https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=3#/',
#'https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=4#/','https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=5#/','https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=6#/']
urls = []
for i in range(1,342):
   st = str('https://batdongsan321.com/nha-dat-ban/ha-noi?category=3&page=' + str(i) + '#/')
   urls.append(st)
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"vi-VN"})
   return bs4.BeautifulSoup(page.content,"html.parser")

for url in urls:
   soup = get_page_content(url)
   houses = soup.findAll('h3', class_='name')
   titles = [house.find('a').text for house in houses]
   price = [pr.text for pr in soup.findAll('span',class_='price')]
   area = [ar.text for ar in soup.findAll('span',class_='area')]
   location = [lct.find('a').text for lct in soup.findAll('span',class_='district')]
   time = [ti.find('li').text for ti in soup.findAll('span',class_ ='meta')]
   df = pandas.DataFrame({
                  'titles':titles, 
                  'price':price, 
                  'area':area,
                  'location':location,
                  'time': time})
   data = pandas.read_csv("testData.csv")
   data = data.append(df,ignore_index = True)
   data.to_csv("testData.csv",index=False)   