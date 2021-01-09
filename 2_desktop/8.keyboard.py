import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("nodocoding", interval=1)
# pyautogui.write("한글은안됌.", interval=1)

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "1", "a", "enter", "enter", "enter"], interval=0.25)


# pyautogui.keyDown("shift")
# pyautogui.press("5")
# pyautogui.keyUp("shift")
#
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl", "a")

pyperclip.copy("나도코딩, ")
pyautogui.hotkey("ctrl", "v")


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


for w in range(100):
    my_write("너도코딩")
    if w % 10 == 0:
        pyautogui.write(["enter"])
