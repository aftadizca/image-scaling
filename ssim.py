import cv2
from skimage.metrics import structural_similarity

img1 = cv2.imread("E:\Images\WALLPAPER\wp8352437_[7680x4320]_denoise].png") #jpg
img2 = cv2.imread("E:\Images\WALLPAPER\wp8352437_[7680x4320]_denoise].webp") #png

ssim_score = structural_similarity(img2, img1, channel_axis=2) #score: 0.0018769083894301646
print(ssim_score)