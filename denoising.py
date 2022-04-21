import cv2
import os
import time
# import matplotlib.pyplot as plt

# print(cv2.__version__)
# Read image
imgPath = "2021317163214_edsr2x.png"
imgPathSplit = os.path.basename(imgPath).split(".")

img = cv2.imread(imgPath)
result = cv2.fastNlMeansDenoisingColored(img, None, 3, 3, 7, 21)

start = time.time()

outputPath = "{0}_denoise.png".format(imgPathSplit[0], imgPathSplit[1])
# print(outputPath)
cv2.imwrite(outputPath, result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
end = time.time()
print("Done in ", end-start, "ms")
