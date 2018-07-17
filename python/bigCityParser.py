from bs4 import BeautifulSoup
import urllib.request
import lxml

html = urllib.request.urlopen("http://www.citymayors.com/statistics/largest-cities-population-125.html").read()
page = BeautifulSoup(html, 'lxml')
page.prettify()

tables = page.find_all('table', width='515')    # looking for the one specific table that contains data about cities
trRows = []
trTags = []
cities = {}

for table in tables:
    trTags = table.find_all('tr')
#
# for i in trTags:
#     trRows.append(i)

for f in trTags:
    trRows.append(f.find_all('font'))

for i in trRows:
    city = i[1].string
    pop = i[3].string
    cities[city] = pop

# Saving cities to file
with open('cities.csv', 'w') as csv:
    for key, value in cities.items():
        csv.write(str(key) + ";" + str(value) + "\n")
csv.close()