from tkinter import image_names
import cv2
import pyautogui
import keyboard
import time
IMAGE = cv2.imread("bild.png")
CROP_W = 679
CROP_H = 1080
(H, W) = IMAGE.shape[:2]
W_ADD = W//2
H_ADD = (H - CROP_H) // 2
IMAGE_NAMES = []
UPLOAD = (1090, 700)
PUBLISH = (1520, 900)
BUTTON_COLOR = (254, 44, 85)
UPLOADED = (1344, 557)
UPLOADED_COLOR = (254, 61, 98)
OPEN_BUTTON = (1560, 300)
for crop in range(3):
    start_x = CROP_W*crop + (W_ADD - CROP_W)
    CROP = IMAGE[0:1080, start_x:CROP_W + start_x]
    name = "cropx.png"
    name = name.replace("x", str(crop))
    print(name)
    cv2.imwrite(name, CROP)

for image in range(3):
    vid_name = "!xuploaded by robot.mp4"
    img_name = "cropx.png"
    vid_name = vid_name.replace("x", str(image))
    img_name = img_name.replace("x", str(image))
    IMAGE_NAMES.append(vid_name)
    video = cv2.VideoWriter(vid_name, 0, 1, (CROP_W, CROP_H))
    for y in range(5):
        video.write(cv2.imread(img_name))
        
print(IMAGE_NAMES)
while True:
    screen = pyautogui.screenshot()
    if screen.getpixel((UPLOAD)) == BUTTON_COLOR:
        pyautogui.click(UPLOAD)
        time.sleep(0.5)
        keyboard.write(IMAGE_NAMES[-1], 0.05)
        IMAGE_NAMES.pop(-1)
        time.sleep(0.5)
        pyautogui.click((1488, 302))
        pyautogui.click(OPEN_BUTTON)
        screen = pyautogui.screenshot()
        if screen.getpixel(PUBLISH) == BUTTON_COLOR:
            pyautogui.click(PUBLISH)
            time.sleep(0.4)
            screen = pyautogui.screenshot()
            if screen.getpixel(UPLOADED) == UPLOADED_COLOR:
                pyautogui.click(UPLOADED)
                time.sleep(0.4)
    time.sleep(2)
    
print("Done")