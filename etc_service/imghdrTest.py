#	이미지인지 확인하려면? ― imghdr
import imghdr
import os

for filename in os.listdir():
    if not os.path.isdir(filename):
        img_type = imghdr.what(filename)
        if img_type:
            os.rename(filename, filename+'.'+img_type)