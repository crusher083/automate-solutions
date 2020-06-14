import os
from bs4 import BeautifulSoup
import requests
import re
from random import choice


def find_srcs(tag):
    url = re.compile(r'(live.staticflickr.com/)(.*)(_n|_m|_q|_w)(\.jpg)')
    srcs = []
    res = requests.get(f"https://www.flickr.com/search/?text={tag}&per_page=1000q")
    res.raise_for_status()
    soup = BeautifulSoup(res.text, features='lxml')
    links = soup.select("div[style*='.jpg']")
    for link in links:
        s = re.search(url, link.get('style'))
        try:
            src = ''.join([s.group(1), s.group(2), '_b_d', s.group(4)])
            srcs.append(src)
        except AttributeError:
            print("I found all images! :D")
    return srcs


def save_folder(tag, srcs, n):
    os.makedirs(f'{tag}', exist_ok=True)
    for i in range(n):
        url = choice(srcs)
        print('Downloading ' + url)
        res = requests.get('http://' + url)
        res.raise_for_status()
        image = open(os.path.join(f'{tag}', os.path.basename(url)), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close()


def random_img():
    tag = input('Choose image tag\n')
    n = int(input('How many images?(1 to 500) '))
    srcs = find_srcs(tag)
    save_folder(tag, srcs, n)
    print('Done')


if __name__ == '__main__':
    random_img()