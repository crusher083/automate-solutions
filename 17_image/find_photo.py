#! python3
import os
from PIL import Image

path = ''
extensions = ['.jpg', '.png', '.gif', '.bmp']


def search_photo(path, extensions):
    for foldername, subfolders, filenames in os.walk(path):
        num_photo = 0
        num_other = 0
        for filename in filenames:
            # Check if file extension isn't .png or .jpg.
            if not any(ext in filename.lower() for ext in extensions):
                num_other += 1
                continue  # skip to next filename
            # Open image file using Pillow.
            else:
                try:
                    im = Image.open(os.path.join(foldername, filename))
                    im_w, im_h = im.size
                    # Check if width & height are larger than 500.
                    if im_w > 500 and im_h > 500:
                        # Image is large enough to be considered a photo.
                        num_photo += 1
                    else:
                        # Image is too small to be a photo.
                        num_other += 1
                except OSError:
                    num_other += 1
        if num_photo > num_other:
            print(foldername)
