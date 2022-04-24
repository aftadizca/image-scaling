from pathlib import Path
import os
import sys

path = "E:\Images\WALLPAPER\\01_SlideShow"
for x in os.listdir(path):
    print(Path(os.path.join(path,x)).exists(),"\t",x)
    if not Path(os.path.join(path,x)).exists():
        print("Deleting ",x)
        os.remove(os.path.join(path,x))