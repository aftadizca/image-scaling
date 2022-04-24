import os
import sys

if not os.path.exists(sys.argv[1]):
    print("Path not exist")
    exit()

srcPath = sys.argv[1]
dstPath = os.path.join("E:\Images\WALLPAPER\\01_SlideShow",os.path.basename(srcPath))

os.symlink(srcPath, dstPath)