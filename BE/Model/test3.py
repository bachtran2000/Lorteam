import bs4
import pandas
import requests

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'vi',
	'Connection': 'keep-alive',
	'Host': 'batdongsan.com.vn',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'
}

url_t = 'https://batdongsan.com.vn'
urls = []
for i in range(1,2):
	st = str('https://batdongsan.com.vn/ban-dat-dat-nen/p' + str(i))
	urls.append(st)


def get_page_content(url):
	page = requests.get(url, headers=headers)
	return bs4.BeautifulSoup(page.content, "html.parser")


df = pandas.DataFrame()
for url in urls:
		soup = get_page_content(url)
		houses = soup.findAll('h3', class_='product-title')
		a_tags = [house.find('a') for house in houses]
		for a_tag in a_tags:
				link = url_t + a_tag.get('href')
				sub_soup = get_page_content(link)
				title = sub_soup.find('h1', class_="tile-product")
				if (title is not None):
						title = title.text
				else:
						continue
				location = sub_soup.find('div', class_="short-detail").text
				i = len(location)
				vitri = location.rfind(',',0,i)
				i = vitri
				vitri = location.rfind(',',0,i)
				
				quan = location[(vitri+2):i]
				
					
				detail = sub_soup.findAll('span', class_='sp2')
				price = detail[0].text
				if(len(detail) > 1):
						area = detail[1].text
				else:
						area = ""
				if(len(detail) > 2):
						nobed = detail[2].text
				else:
						nobed = 0
				describe = sub_soup.find('div', class_='des-product').text
				box_round = sub_soup.findAll('div', class_='box-round-grey3')

				box_round_1 = box_round[0].findAll('span', class_='r1')
				box_round_1_2 = box_round[0].findAll('span', class_='r2')
				for i in range(len(box_round_1)):
						box_round_1[i] = box_round_1[i].text
				if('Số toilet:' in box_round_1):
						notoilet = box_round_1_2[box_round_1.index(
							'Số toilet:')].text
				else:
						notoilet = ""
				if('Mặt tiền:' in box_round_1):
						mattien = box_round_1_2[box_round_1.index(
							'Mặt tiền:')].text
				else:
						mattien = ""
				if('Đường vào:' in box_round_1):
						duongvao = box_round_1_2[box_round_1.index(
							'Đường vào:')].text
				else:
						duongvao = ""
				if('Số tầng:' in box_round_1):
						sotang = box_round_1_2[box_round_1.index(
							'Số tầng:')].text
				else:
						sotang = ""
				if('Hướng nhà:' in box_round_1):
						huong_nha = box_round_1_2[box_round_1.index(
							'Hướng nhà:')].text
				else:
						huong_nha = ""
				if('Hướng ban công:' in box_round_1):
						huong_ban_cong = box_round_1_2[box_round_1.index(
							'Hướng ban công:')].text
				else:
						huong_ban_cong = ""
				if('Nội thất:' in box_round_1):
						noi_that = box_round_1_2[box_round_1.index(
							'Nội thất:')].text
				else:
						noi_that = ""
				chudautu = ""
				quymo = ""
				if(len(box_round) > 1):
						row_1 = box_round[1].findAll('span', class_='r1')
						row_2 = box_round[1].findAll('span', class_='r2')
						for i in range(len(row_1)):
								row_1[i] = row_1[i].text
						if('Chủ đầu tư:' in row_1):
								index = row_1.index('Chủ đầu tư:')
								chudautu = row_2[index].text
						if('Quy mô:' in row_1):
								index = row_1.index('Quy mô:')
								quymo = row_2[index].text
				short_detail_2 = sub_soup.find(
					'ul', class_='short-detail-2 list2 clearfix')
				time = short_detail_2.findAll('span', class_='sp3')
				ngaydang = time[0].text
				ngayhet = time[1].text
				loaitin = time[2].text
				phone = sub_soup.find('span', class_='phoneEvent').get('raw')
				coordinate_div = sub_soup.find('div', class_='map')
				image_tag = sub_soup.findAll('img',class_ = 'img-responsive')
				if(image_tag is not None):
					for i in range(len(image_tag)):
						image_tag[i] = image_tag[i].get('src-lazy')
					image_tag = [image_tag]
				else:
					image_tag = []

				if(coordinate_div is not None):
						coordinate_iframe = coordinate_div.find('iframe').attrs['src']   
						head = coordinate_iframe.index('q=') + 2
						tail = coordinate_iframe.index('&key')
						coordinate = coordinate_iframe[head:tail].split(",")
						latitude = coordinate[0]
						longitude = coordinate[1]

				df = df.append(pandas.DataFrame({
						'TieuDe': pandas.Series(title),
						'url': pandas.Series(link),
						'ViTri': pandas.Series(location),
						'Quan':pandas.Series(quan),
						'GiaTien': pandas.Series(price),
						'DienTich': pandas.Series(area),
						'SoPhongNgu': pandas.Series(nobed),
						'SoToilet': pandas.Series(notoilet),
						'HinhAnh': pandas.Series(image_tag),
						#'MatTien': pandas.Series(mattien),
						#'DuongVao': pandas.Series(duongvao),
						#'SoTang' : pandas.Series(sotang),
						'HuongNha': pandas.Series(huong_nha),
						'HuongBanCong': pandas.Series(huong_ban_cong),
						'NoiThat': pandas.Series(noi_that),
						'MoTa': pandas.Series(describe),
						'Chudautu': pandas.Series(chudautu),
						'QuyMo': pandas.Series(quymo),
						'ViDo': pandas.Series(latitude),
						'KinhDo': pandas.Series(longitude),
						'NgayDang': pandas.Series(ngaydang),
						'LoaiTin': pandas.Series(loaitin),
						'DienThoai': pandas.Series(phone)}))
df.to_csv("nhadat.csv",index=False)   
