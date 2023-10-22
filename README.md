# retroarch-overlay-resize (for Steam Deck)
This is a python script that scans the current images for retroarch overlay images and resizes them to fit in a different screen sizes. It also creates the corresponding cfg file that you can load from Retroarch.

I created it to make overlays for my Steam Deck, which has a 800p screen (1280x800) and most of the overlays I could found were in 16:9 aspect ratio.

Currently it produces two versions:

- Straight up resized image, which will have some distortion due to the stretching. Since the conversion is not that significant (16:9 -> 16:10) it usually isn't that noticeable.
- Cropped. This means it's resized to fit the height only, then it's cropped to the center. While this retains the image ratio, it cuts off the left and right sides.

## how to use:

Install Pillow

```
pip install pillow
```

Put the script to the directory that only has overlay images. Then run the script.

```
python convert.py
```
