import os

srcPath = "E:\Images\WALLPAPER\Genshin\\2022422185550_[8192x4096].png"
dstPath = os.path.join("E:\Images\WALLPAPER\\01_SlideShow",os.path.basename(srcPath))

os.symlink(srcPath, dstPath)