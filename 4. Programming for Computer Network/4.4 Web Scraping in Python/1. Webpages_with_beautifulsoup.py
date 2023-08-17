import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=python+http+request"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href'))

print('\nWill retrieve all h3>div contents\n')    
h3tags = soup('h3')
for h3 in h3tags:
    print(h3.find('div').text)
    
    # will retrieve the parent tags
    print(h3.parent)