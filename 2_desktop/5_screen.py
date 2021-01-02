import pyautogui

# 화면 스크린 샷 만들기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()

# 3059,19 60,63,65 #3C3F41
try:
    pixel = pyautogui.pixel(3059, 19)
    print(pyautogui.pixelMatchesColor(3059, 19, pixel))
except:
    print("error")


