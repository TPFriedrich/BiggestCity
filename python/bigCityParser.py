
"""
This script is downloading data about cities population and saves it to CSV file
"""

from bs4 import BeautifulSoup
import urllib.request
import lxml

# Retrieving data from FIRST page
html = urllib.request.urlopen("http://www.citymayors.com/statistics/largest-cities-population-125.html").read()
page = BeautifulSoup(html, 'lxml')
page.prettify() # Just to format/justify the html

# Table with the first 150 cities
tables = page.find_all('table', width='515')    # looking for the one specific table that contains data about cities

# Retrieving data from NEXT page
nextPage = page.find_all('a', string='NEXT')    # Looking for a link with string NEXT
nextLink = nextPage[0]['href']  # getting link from HREF attribute
nextPageLink = "http://www.citymayors.com/statistics/" + nextLink    # calculating link to next page
htmlNextPage = urllib.request.urlopen(nextPageLink).read()  # retrieving html from NEXT address
nextPageContent = htmlNextPage = BeautifulSoup(htmlNextPage, 'lxml')
nextPageContent.prettify()

# Table with the last 150 cities
tablesNext = nextPageContent.find_all('table', width='515')

# Temporary list for TR tags
trRows = []
trTags = []
cities = {} # dictionary to keep cities data

# Retrieving all rows - TR, from the first table
for table in tables:
    trTags = table.find_all('tr')

# Retrieving all rows - TR, from the second table and it to list [not overwriting]
for tableN in tablesNext:
    trTags = trTags + tableN.find_all('tr')

# Now we are searching through the TR tags and looking for the FONT tags.
# Each element on the list below contains one row from table. One row is:
#   [0]   [1]       [2]        [3]            [4]
#   Nr   City     Country   Population      Metropoly population
#  175 WARSAW 	Poland 	    1,749,000       3,101,000
#
# We need only city name and population.
for f in trTags:
    trRows.append(f.find_all('font'))

# iterating through TR list and getting name of the cities and population
#
for i in trRows:
    city = i[1].string
    pop = i[3].string
    cities[city] = pop

# Saving cities to file
with open('cities.csv', 'w') as csv:
    for key, value in cities.items():
        csv.write(str(key) + ";" + str(value) + "\n")
csv.close()