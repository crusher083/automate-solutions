#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def download(start_com, end_com):
    for url_num in range(start_com, end_com):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % url_num)
        res = requests.get('http://xkcd.com/%s' % url_num)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            com_url = comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (com_url))
            res = requests.get(com_url)
            res.raise_for_status()
            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(com_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


# Create and start the Thread objects.
down_threads = []  # a list of all the Thread objects
for i in range(0, 1400, 100):  # loops 14 times, creates 14 threads
    down_thread = threading.Thread(target=download, args=(i, i + 99))
    down_threads.append(down_thread)
    down_thread.start()

# Wait for all threads to end.
for down_thread in down_threads:
    down_thread.join()
print('Done.')