from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("http://www.citymayors.com/statistics/largest-cities-population-125.html").read()
page = BeautifulSoup(html, 'html.parser')
page.prettify()

tables = page.find_all('table', width='515')    # looking for the one specific table that contains data about cities
trRows = []
#print(tables)


for table in tables:
    trTags = table.find_all('tr')
#
# for i in trTags:
#     trRows.append(i)

print(trTags)