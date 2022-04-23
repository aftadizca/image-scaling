import cv2
import os
import time
import argparse


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


info = colors.fg.yellow+colors.bold+"[INFO]"+colors.reset

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Path to the Image")
parser.add_argument("-r", "--res", type=int,
                    help="Rescaling resolution Max. 4")

args = parser.parse_args(["E:\\test.jpg"])
print(args)

# Read image
img = cv2.imread(args.path)

# Get image resolution
w = img.shape[1]
h = img.shape[0]
print()
print(info, "Image Resolution \t: ", w, " x ", h)

start = time.time()

# Get rescaling factor
rescale = args.res if args.res else min(round(8000/w), 4)
print(info, "Rescale Factor \t\t: ", rescale)

# Get info img path
imgFolderPath = os.path.split(args.path)[0]
imgPathSplit = os.path.basename(args.path).split(".")

# Read model path
pathModel = "model/EDSR_x{0}.pb".format(rescale)
modelName = os.path.split(pathModel)[-1].split("_")[0].lower()
modelMultiply = os.path.split(pathModel)[-1].split("_")[1][1]

# Upscaling
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(pathModel)
sr.setModel(modelName, int(modelMultiply))
result = sr.upsample(img)

outputPath = "{4}\{0}_[{2}x{3}].png".format(
    imgPathSplit[0], imgPathSplit[1], result.shape[1], result.shape[0], imgFolderPath)

cv2.imwrite(outputPath, result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
end = time.time()
totalTime = end-start
print(info, "Done in {0}m {1}s".format(
    int(totalTime//60), int(totalTime % 60)))
