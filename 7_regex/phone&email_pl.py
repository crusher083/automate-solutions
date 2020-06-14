#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip
import re

phoneRegex = re.compile(r'''(
(\+48)?              # country code
(\s)?
(\d{2}|\(\d{2}\))?
(\s)?                # area code
(\d{3})              # first 3 digits
(\s|-|\.)            # separator
(\d{2,3})
(\s|-|\.)
(\d{2,3})
)''', re.X)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@                 # @ symbol
[a-zA-Z0-9.-]+    # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.X)

peselRegex = re.compile
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[5], groups[7], groups[9]])
    if groups[3] != '':
        phoneNum = groups[3] + ' ' + phoneNum
    elif groups[10] != '':
        phoneNum += ' ' + groups[10]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
