import requests
from bs4 import BeautifulSoup

http = ['http://', 'https://']
good = 0
broken = 0
res = requests.get("https://arstechnica.com")
res.raise_for_status()
soup = BeautifulSoup(res.text, features='lxml')
links = [(str(elem.get('href'))) for elem in soup.find_all('a')]
links_no_doubles = list(set(links))
for pref in http:
    for link in links_no_doubles:
        if pref in link:
            res1 =  requests.get(link)
            try:
                res1.raise_for_status()
                good += 1
                print(link)
            except requests.exceptions.HTTPError as err:
                print(f'Broken: {link}')
                broken += 1
print(f'{broken} broken links')