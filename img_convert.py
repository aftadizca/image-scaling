import cv2
import os
import time

imgPath = "E:\Images\WALLPAPER\Genshin\\202131713108_[8192x4096].png"
imgFolderPath = os.path.split(imgPath)[0]
imgPathSplit = os.path.basename(imgPath).split(".")

img = cv2.imread(imgPath)
start = time.time()

outputPath = "{2}\{0}_Q200.webp".format(
    imgPathSplit[0], imgPathSplit[1],imgFolderPath)
# print(outputPath)
# cv2.imwrite(outputPath, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
# cv2.imwrite(outputPath, result, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite(outputPath, img, [cv2.IMWRITE_WEBP_QUALITY, 200])
# cv2.imwrite(outputPath, result)

end = time.time()
print("Done in ", end-start, "s")
