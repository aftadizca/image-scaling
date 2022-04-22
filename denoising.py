import cv2
import os
import time
# import matplotlib.pyplot as plt

# print(cv2.__version__)
# Read image
imgPath = "E:\Images\WALLPAPER\Claris HD\\1200_[4800x2700].png"
imgFolderPath = os.path.split(imgPath)[0]
imgPathSplit = os.path.basename(imgPath).split(".")

img = cv2.imread(imgPath)
result = cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 7, 21)

start = time.time()

outputPath = "{2}\{0}_denoise.png".format(
    imgPathSplit[0], imgPathSplit[1],imgFolderPath)
# print(outputPath)
cv2.imwrite(outputPath, result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
# cv2.imwrite(outputPath, result, [cv2.IMWRITE_JPEG_QUALITY, 100])
# cv2.imwrite(outputPath, result, [cv2.IMWRITE_WEBP_QUALITY, 200])
cv2.imwrite(outputPath, result)

end = time.time()
print("Done in ", end-start, "s")
