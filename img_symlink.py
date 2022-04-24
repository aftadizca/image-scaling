import os

srcPath = "E:\Images\WALLPAPER\Genshin\wp8352437_[7680x4320]_denoise].webp.png"
dstPath = os.path.join("E:\Images\WALLPAPER\\01_SlideShow",os.path.basename(srcPath))

os.symlink(srcPath, dstPath)