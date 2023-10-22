from PIL import Image
import os, sys

dir = os.getcwd() # current folder
width = 1280 # target width
height = 800 # target height
original_ratio = 16/9


def create_cfg(filename):
    filename = filename.rsplit('/', 1)[1]
    cfg_file = filename + ".cfg"
    with open(cfg_file, 'w') as f:
        f.write("""
overlays = 1

overlay0_overlay = %s.png


overlay0_full_screen = true

overlay0_descs = 0
""" %filename)

# resizes the images found in the folder to 1280x800 with rataining the original image ratio, which means it will be cropped to the center, losing some image on both left and right sides.
def resize_with_crop(filelist):
    for item in filelist:
        item_path = dir +"/" + item
        if os.path.isfile(item_path):
            
            if ".png" in item_path:
                with open(item_path, "rb") as imgFile:
                    img = Image.open(imgFile)
                    filename, extention = os.path.splitext(item_path)

                    ## we first want to down to 1422x800 to retain the ratio but reduce the overall size to fit the height of steam deck
                    temp_width = int(height*original_ratio)
                    resized_image = img.resize((temp_width, height), Image.Resampling.LANCZOS)

                    # Attempt to rename the original file
                    filename = filename.replace('16x9', "16x10").replace("2560x1440", "1280x800").replace("1920x1080", "1280x800") + "-cropped"

                    # Crop at the center, retaining the ratio
                    crop_left = (temp_width - width) / 2
                    crop_right = crop_left + width
                    cropped_image = resized_image.crop((crop_left, 0, crop_right, height))
                    cropped_image.save(filename + '.png')

                    create_cfg(filename)

# resizes the images found in the folder to 1280x800 without retaining the original ratio.
def resize(filelist):
    for item in filelist:
        item_path = dir +"/" + item
        if os.path.isfile(item_path):
            
            if ".png" in item_path:
                with open(item_path, "rb") as imgFile:
                    img = Image.open(imgFile)
                    filename, extention = os.path.splitext(item_path)
                    resized_image = img.resize((width, height), Image.Resampling.LANCZOS)

                    # Attempt to rename the original file
                    filename = filename.replace('16x9', "16x10").replace("2560x1440", "1280x800").replace("1920x1080", "1280x800") + '-resized'
                    resized_image.save(filename + '.png') 

                    create_cfg(filename)

filelist = os.listdir(dir)
resize(filelist)
resize_with_crop(filelist)
