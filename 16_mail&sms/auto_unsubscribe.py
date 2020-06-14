from imapclient import IMAPClient
import imaplib
from pyzmail import PyzMessage
from bs4 import BeautifulSoup
import webbrowser


def find_urls(imap_dom, mail, password):
    url = []
    imaplib._MAXLINE = 10_000_000
    imap = IMAPClient(imap_dom, ssl=True)
    imap.login(mail, password)
    imap.select_folder('INBOX', readonly=True)
    uids = imap.search(['SINCE', '01-Mar-2020'])
    for n in uids:
        raw_messages = imap.fetch([n], ['BODY[]'])
        message = PyzMessage.factory(raw_messages[n][b'BODY[]'])
        if message.html_part:
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = BeautifulSoup(html, 'lxml')
            links = soup.select('a')
            for link in links:
                if 'unsubscribe' in link.text.lower():
                    url.append(link.get('href'))
    imap.logout()
    return url


def open_links(links):
    for link in links:
        print(f'Opening {link}...')
        webbrowser.open(link)


if __name__ == '__main__':
    urls = find_urls(mail, password)
    open_links(urls)





