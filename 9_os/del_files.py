import os

for foldername, subfolder, filenames in os.walk(path):
    for filename in filenames:
        full_path = os.path.join(foldername, filename)
        filesize = os.path.getsize(foldername + '\\' + filename)
        if filesize > (1024**2) * 100:
            print('Deleting ' + filename)
