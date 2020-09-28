import requests
from bs4 import BeautifulSoup
import csv

url = 'https://moz.com/top500'

response = requests.get(url)
#print(response.status_code)
#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find_all('table', class_ = 'table table-responsive-md table-bordered table-zebra mb-5')#get the table

table = table[0]


with open ('website_urls.csv','w') as r:
    for row in table.find_all('tr'):      #in every row find all other columns
        for cell in row.find_all('a'):
            writer = csv.writer(r)
            writer.writerow([cell.text]) #should be in the list format