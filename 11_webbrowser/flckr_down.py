import os
from bs4 import BeautifulSoup
import requests
import re

def find_srcs(tag, n):
    url = re.compile(r'(live.staticflickr.com/)(.*)(_n|_m|_q|_w)(\.jpg)')
    srcs = []
    res = requests.get(f"https://www.flickr.com/search/?text={tag}&per_page={n + 25}")
    res.raise_for_status()
    soup = BeautifulSoup(res.text, features='lxml')
    links = soup.select("div[style*='.jpg']")
    for link in links:
        s = re.search(url, link.get('style'))
        src = ''.join([s.group(1), s.group(2), '_b_d', s.group(4)])
        srcs.append(src)
        if len(srcs) == n:
            break
    return srcs


def save_folder(tag, srcs):
    os.makedirs(f'{tag}', exist_ok=True)
    for url in srcs:
        print('Downloading ' + url)
        res = requests.get('http://' + url)
        res.raise_for_status()
        image = open(os.path.join(f'{tag}', os.path.basename(url)), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close()


def flckr_scrap():
    tag = input('Choose image tag\n')
    n = int(input('How many images? '))
    srcs = find_srcs(tag, n)
    save_folder(tag, srcs)
    print('Done')


if __name__ == '__main__':
    flckr_scrap()