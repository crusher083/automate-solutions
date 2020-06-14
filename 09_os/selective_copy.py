#!python 3

import os
import shutil

src = os.path.dirname(os.path.abspath(__file__))
dst = dst
if not os.path.exists(dst):
    os.makedirs(dst)
for foldername, subfolder, filenames in os.walk(src):
    print('Checking ' + os.path.join(src, foldername))
    for filename in filenames:
        if filename.endswith('.txt'):
            print(f'Copying {filename} from {foldername} to {dst}...')
            shutil.copyfile(os.path.join(foldername, filename),
                            os.path.join(dst, filename))
