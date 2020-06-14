#! python3
# lucky.py - Opens several Google search results.
import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links
soup = BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result
link_elems = soup.select('div#main > div > div > div > a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))