# This is a simple implementation of web scraping using requests and BeautifulSoup, to extract the
# current time of the 143 most popular cities in the world

import requests
from bs4 import BeautifulSoup

print("enter the city name")
city=input()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8"

r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.content,'html.parser')


location =  soup.select('#wob_loc')[0].getText().strip()
time =  soup.select('#wob_dts')[0].getText().strip()
info = soup.select('#wob_dc')[0].getText().strip()
weather = soup.select('#wob_tm')[0].getText().strip()


print(location,time,info,weather)
# World_clock = []
# i=0
# j=1

# tags = soup.find_all('td')


# for tag in tags:

#     city = tags[i].find('a')
#     time = tags[j]
#     World_clock.append(f"{city}, {time}")
#     i+=2
#     j+=2

# World_clock.sort()

# for item in range(0,len(World_clock)):
#     print(World_clock[item])

