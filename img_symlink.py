import os

srcPath = "E:\Images\WALLPAPER\Kurumi\kurumi_denoise.png"
dstPath = os.path.join("E:\Images\WALLPAPER\\01_SlideShow",os.path.basename(srcPath))

os.symlink(srcPath, dstPath)