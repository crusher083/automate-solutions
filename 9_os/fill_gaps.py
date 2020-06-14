import os
import shutil
import re
from collections import Counter
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -\
%(levelname)s- %(message)s')

# Works for different prefixes
# Needs fix for extensions

numb_re = re.compile(r'''
    (\D*?)         # name
    (\d*)          # digits inside name
    (\D*?)         # letters
    (\.\w*)        # format
    ''', re.X | re.I)

folder = 'D:\\Python\\09_fill_gaps'
found = []
prefixes = []
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        m = re.search(numb_re, filename)
        prefix = m.group(1)
        prefixes.append(prefix)
        num = m.group(2)
        found.append(num)
        f_format = m.group(4)
    order = [int(x) for x in found]
ordered_names = []
for prefix, code in dict(Counter(prefixes)).items():
    for num in range(1, code + 1):
        zeros = '0' * (len(found[0]) - len(str(num)))
        current_file = '{}/{}{}{}{}'.format(folder, prefix, zeros,
                                            num, f_format)
        if os.path.exists(current_file) is False:
            for i in range(1, len(order) + 1):
                next_num = order[i - 1]
                next_zeroes = '0' * (len(found[0]) - len(str(next_num)))
                next_file = (folder + '/' + prefix + str
                             (next_zeroes) + str(next_num) + f_format)
                print(next_file)
                shutil.move(next_file, current_file)
