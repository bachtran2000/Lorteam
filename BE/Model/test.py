import bs4
import pandas
import requests

url = 'https://www.muabannhadat.vn/mua-ban-bat-dong-san' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
url1 = 'https://www.muabannhadat.vn/mua-ban-bat-dong-san?page=2'
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"vi-VN"})
   return bs4.BeautifulSoup(page.text,"html.parser")

soup = get_page_content(url)
soup = get_page_content(url1)
houses = soup.findAll('h3', class_="uppercase text-red text-base leading-normal mb-1")
titles = [house.find('a').text for house in houses]

detail = [ce.text for ce in soup.findAll('h5',class_='uppercase leading-normal mb-1 text-xs')]
area = [rt.text for rt in soup.findAll('span',class_='text-sm text-black mr-5')]

noBed = [gr.text for gr in soup.findAll('span',class_="text-sm text-black mr-5")]

bath = [gr.text for gr in soup.findAll('span',class_="text-sm text-black")]

prices = [gr.text for gr in soup.findAll('span',class_="font-bold mr-5")]
a = {'titles' : titles ,'detail' : detail , 'area': area , 'numberofBedroom':noBed , 'bath' : bath,'price':prices}
df = pandas.DataFrame.from_dict(a, orient='index')
df.transpose()
df.to_csv('export_data.csv',index=False,header= True)