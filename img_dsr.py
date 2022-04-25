import cv2
import os
import time
import argparse
import numpy as np


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


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    # For details on unsharp masking, see:
    # https://en.wikipedia.org/wiki/Unsharp_masking
    # https://homepages.inf.ed.ac.uk/rbf/HIPR2/unsharp.htm
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


info = colors.bg.green+colors.bold+" [INFO] "+colors.reset
middle = colors.bg.blue+colors.fg.lightgrey

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Path to the Image")
parser.add_argument("-u", action='store_true',
                    help="Do rescale")
parser.add_argument("-uf", type=int,
                    help="Rescaling factor (max. 4)")

parser.add_argument("-d", action='store_true',
                    help="Do denoising (default: 3 3 7 21)")
parser.add_argument("-dh", type=int, default=3,
                    help="h params for denoise  (default: 3)")
parser.add_argument("-dhc", type=int, default=3,
                    help="hColor params for denoise  (default: 3)")
parser.add_argument("-dtw", type=int, default=7,
                    help="templateWindowSize params for denoise  (default: 7)")
parser.add_argument("-dsw", type=int, default=21,
                    help="searchWindowSize params for denoise  (default: 21)")

parser.add_argument("-s", nargs='?', type=float, default=None, const=5.0,
                    help="searchWindowSize params for denoise  (default: 0.5)")

parser.add_argument("-png", nargs='?', type=int, default=None, const=9,
                    help="For PNG, it can be the compression level from 0 to 9 [default: 9]")
parser.add_argument("-webp", nargs='?', type=int, default=None, const=200,
                    help="For WEBP, it can be a quality from 1 to 100 (the higher is the better). By default (without any parameter) \
                        and for quality above 100 the lossless compression is used. [default: 200]")
parser.add_argument("-jpg", nargs='?', type=int, default=None, const=100,
                    help="For JPEG, it can be a quality from 0 to 100 (the higher is the better) [default: 100]")


# args = parser.parse_args("E:\Images\WALLPAPER\Claris HD\\1200_[4800x2700]_denoise.png -webp".split())
args = parser.parse_args()


# print(args)
# exit()

# Read image
if not os.path.exists(args.path):
    print("Image path not found")
    exit()
img = cv2.imread(args.path)

# Get image resolution
w = img.shape[1]
h = img.shape[0]
print()
print(info, "Image Resolution \t: ", w, " x ", h)

start = time.time()

# create output img path
ext = args.path.rfind(".")
outputPath = args.path[:ext]

if args.u:
    print(info, middle, "UPSCALING IMAGE \t", colors.reset)
    # Get rescaling factor
    rescale = args.uf if args.uf else min(round(8000/w), 4)
    print(info, "Rescale Factor \t\t: ", rescale)

    # Read model path
    pathModel = "D:\PROGRAMMING\image-scaling\image-scaling\model\EDSR_x{0}.pb".format(
        rescale)
    modelName = os.path.split(pathModel)[-1].split("_")[0].lower()
    modelMultiply = os.path.split(pathModel)[-1].split("_")[1][1]

    # Upscaling
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(pathModel)
    sr.setModel(modelName, int(modelMultiply))
    img = sr.upsample(img)

    outputPath = "{0}_{1}x{2}".format(outputPath, img.shape[1], img.shape[0])

if args.s:
    print(info, middle, "SHARPENING IMAGE \t", args.s, colors.reset)
    img = unsharp_mask(img, amount=args.s)
    outputPath = "{0}_sharp".format(outputPath)

if args.d:
    print(info, middle, "DENOISING IMAGE \t", args.dh,
          args.dhc, args.dtw, args.dsw, colors.reset)
    img = cv2.fastNlMeansDenoisingColored(
        img, None, args.dh, args.dhc, args.dtw, args.dsw)
    outputPath = "{0}_denoise".format(outputPath)

if args.png:
    print(info, middle, "SAVE AS PNG \t", colors.reset)
    cv2.imwrite(outputPath+".png", img,
                [cv2.IMWRITE_PNG_COMPRESSION, args.png])
elif args.webp:
    print(info, middle, "SAVE AS WEBP \t", colors.reset)
    cv2.imwrite(outputPath+".webp", img, [cv2.IMWRITE_WEBP_QUALITY, args.webp])
    os.rename(outputPath+".webp", outputPath+".webp.png")
elif args.jpg:
    print(info, middle, "SAVE AS JPG \t", colors.reset)
    cv2.imwrite(outputPath+".jpg", img, [cv2.IMWRITE_WEBP_QUALITY, args.jpg])
else:
    print(info, middle, "SAVE AS PNG \t", colors.reset)
    cv2.imwrite(outputPath+".png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

end = time.time()
totalTime = end-start
print(info, "Done in {0}m {1}s".format(
    int(totalTime//60), int(totalTime % 60)))
