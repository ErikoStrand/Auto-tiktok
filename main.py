import cv2

IMAGE = cv2.imread("bild.png")
CROP_W = 679
CROP_H = 1080
(H, W) = IMAGE.shape[:2]
W_ADD = W//2
H_ADD = (H - CROP_H) // 2
for crop in range(3):
    start_x = CROP_W*crop + (W_ADD - CROP_W * 2)
    CROP = IMAGE[0:1080, start_x:CROP_W + start_x]
    if crop == 0:
        cv2.imwrite("crop1.png", CROP)
    if crop == 1:
        cv2.imwrite("crop2.png", CROP)
    if crop == 2:
        cv2.imwrite("crop3.png", CROP)
        
print("Done")