import cv2
import os

path = "D:\KOLEKSI\ANIME\\2. VIDEO ANIME\ClariS 1st Budokan Concert\Scans"

# 

for x in os.listdir(path):
    ex = x.rfind(".")
    filename = x[:ex]
    img = cv2.imread(os.path.join(path,x))
    cv2.imwrite(os.path.join(path,filename+".webp"), img, [cv2.IMWRITE_WEBP_QUALITY, 200])
    os.rename(os.path.join(path,filename+".webp"), os.path.join(path,filename+".webp.png"))