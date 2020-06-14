#! python3

"""Chores assignment auto email"""

from random import choice
from collections import defaultdict as dd
import smtplib
import json


def compare_ddicts(d1, d2):
    d = []
    for key, value in d1.items():
        d1_values = tuple(value)
        d2_values = d2.get(key, ())
        diff = [v for v in d1_values if v in d2_values]
        d.extend(diff)
    return d


def open_log(filename):
    try:
        with open(f'{filename}', 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        log = {}
    return log


def randomizer(chor, mail_list):
    chores_temp = chor[:]
    randomized = dd(list)
    while len(chores_temp) > 0:
        for n in range(len(chor) // len(mail_list)):
            for email in mail_list:
                try:
                    rand = choice(chores_temp)
                    randomized[email].append(rand)
                    chores_temp.remove(rand)
                except IndexError:
                    break
        for i in range(len(chores_temp)):
            randmail = choice(mail_list)
            rand = choice(chores_temp)
            randomized[randmail].append(rand)
            chores_temp.remove(rand)
    return randomized


def send_mail(randomized):
    smtpobj = smtplib.SMTP('smtp.example.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login('bob@example.com', 'password')
    for k, v in randomized.items():
        smtpobj.sendmail('bob@example.com', k, f'Subject: {" and ".join(v).capitalize()}.'
                                               f'\nDon\'t forget to {" and ".join(v)} today!')


def save_log(log):
    with open('chores_log.json', 'w') as update:
        json_file = json.dump(log, update, indent=2)


if __name__ == '__main__':
    last_week = open_log('chores_log.json')
    chores = ['do dishes', 'clean bathroom', 'walk dog', 'vacuum']
    mails = ['dany@example.com', 'mandy@example.com', 'alice@example.com']
    curr_week = randomizer(chores, mails)
    if not compare_ddicts(curr_week, last_week):
        pass
    else:
        curr_week = randomizer(chores, mails)
    send_mail(curr_week)
    save_log(curr_week)
