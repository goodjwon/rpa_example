import pyautogui

fw = pyautogui.getActiveWindow()
print(fw.title)
print(fw.size)
print(fw.left, fw.right,fw.top, fw.bottom)

# for w in pyautogui.getAllWindows():
#     print(w)

for w in pyautogui.getWindowsWithTitle("제목 없음"):
    print(w)
    if not w.isActive:
        w.activate()
    if not w.isMaximized:
        w.maximize()
    pyautogui.sleep(1)
    w.restore()
    w.close()