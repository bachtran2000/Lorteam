# imports
from bs4 import BeautifulSoup
import requests
# scrape the article 
# Defines function to return only ascii characters.
def ascii_only(content):
    return str(''.join(c for c in content if ord(c)<128))
# defines function to get distance/duration to office
def get_distance(stop, start='upwork chicago'):
    api = 'AIzaSyBwZnYN0B2w_H3ZpzcYsAmsaHvAv1s7Xfg'
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + start + "&destinations=" + stop + "&key=" + api
    link = requests.get(url)
    print(link)
    json_loc = link.json()
    distance = json_loc['rows'][0]['elements'][0]['distance']['text']
    duration = json_loc['rows'][0]['elements'][0]['duration']['text']
    return distance, duration
url = 'https://www.builtinchicago.org/companies/best-places-to-work-chicago-2019'
resp = requests.get(url)
page = BeautifulSoup(resp.content, "html.parser")
# Finds company name in each ranking; still needs some cleaning.
heads = page.find_all('div', {'class':'company-header'})
# creates a dictionary where {k,v} = office name, distance
d = {}
for i in heads:
    name = i.find('a').attrs['href'].split('/')[2]

    d[name] = ascii_only(get_distance(name + ' chicago')[0]).split(' ')[0]
#print(d)