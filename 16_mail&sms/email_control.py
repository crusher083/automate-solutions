from imapclient import IMAPClient
import imaplib
from pyzmail import PyzMessage
from subprocess import Popen


def find_instructions(imap_dom, mail, password):
    instructions, remove_id = [], []
    imaplib._MAXLINE = 10_000_000
    imap = IMAPClient(imap_dom, ssl=True)
    imap.login(mail, password)
    imap.select_folder('INBOX', readonly=False)
    uids = imap.search(['SUBJECT', 'control'])
    for item in uids:
        raw_messages = imap.fetch([item], ['BODY[]'])
        message = PyzMessage.factory(raw_messages[item][b'BODY[]'])
        if message.text_part:
            body = message.text_part.get_payload().decode(message.text_part.charset)
            instructions.append(body)

        remove_id.append(id)
    delete_emails(imap, remove_id)
    return instructions


def delete_emails(imap, remove_id):
    if remove_id:
        imap.delete_messages(remove_id)
        imap.expunge()
    imap.logout()


def start_qbit(qbit, email_body):
    lines = email_body.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            torrent_process = Popen([qbit, line])
            torrent_process.wait()


if __name__ == '__main__':
    qbit_path = 'qbittorrent.exe'
    email = EMAIL
    instructions_body = find_instructions(imap_dom='imap.gmail.com',
                                          mail=email,
                                          password=password)
    if instructions_body:
        for instruction in instructions_body:
            start_qbit(qbit_path, instruction)
