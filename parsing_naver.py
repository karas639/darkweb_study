#darkweb crolling study

from bs4 import BeautifulSoup
import requests

url = "http://www.naver.com"
res = requests.get(url)

#result = res.text
result = BeautifulSoup(res.text,'html.parser')

for script in result.find_all('script'):
    script.extract()

navbar = result.find("div", {'class' : 'section_navbar'})
naver = navbar.encode("utf-8").replace("\n","A").replace("\r","B").replace("\t","C")
print(naver)

# div tag parsing
#for i in result.findAll("div"):
#    print(i.get_text())

# ul tag parsing in div tag 
for i in result.findAll("div"):
    for j in i.findAll("ul"):
        print(j.get_text())

#print(result.get_text())

