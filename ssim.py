import cv2
from skimage.metrics import structural_similarity

img1 = cv2.imread("E:\Images\WALLPAPER\Claris HD\\1200_[4800x2700]_denoise.jpg") #jpg
img2 = cv2.imread("E:\Images\WALLPAPER\Claris HD\\1200_[4800x2700]_denoise.png") #png
img3 = cv2.imread("E:\Images\WALLPAPER\Claris HD\\1200_[4800x2700]_denoise.webp") #webp

ssim_score = structural_similarity(img2, img1, channel_axis=2) #score: 0.0018769083894301646
print(ssim_score)

ssim_score = structural_similarity(img2, img3, channel_axis=2) #score: 1.0
print(ssim_score)