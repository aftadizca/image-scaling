import cv2
import os
import time

# Read image
imgPath = "2021317163214.png"
path = "model/LapSRN_x2.pb"

imgPathSplit = os.path.basename(imgPath).split(".")
modelName = os.path.split(path)[-1].split("_")[0].lower()
modelMultiply = os.path.split(path)[-1].split("_")[1][1]

img = cv2.imread(imgPath)

sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(path)

print("[INFO] Using {0} with {1}x rescaling".format(
    modelName.upper(), modelMultiply))

start = time.time()

sr.setModel(modelName, int(modelMultiply))
result = sr.upsample(img)

outputPath = "{0}_[{2}x{3}].png".format(
    imgPathSplit[0], imgPathSplit[1],  result.shape[1], result.shape[0])

cv2.imwrite(outputPath, result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
end = time.time()
print("Done in ", end-start, "s")
