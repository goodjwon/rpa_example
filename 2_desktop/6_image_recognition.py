import time
import sys
import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)


"""
    pyautogui 는 이미지 기반 으로 찾기 때문에 해상독가 높은 경우 느리게 반응 함.
    1. grayscale=True 로 하여 처리
    2. region 으로 범위 지정
    3. 정확도 조정 opencv-python locateOnScreen("file_menu.png") 
        => pip install opencv-python 설치.
        => locateOnScreen("file_menu.png", confidence=0.9)
    4. 참고 : numpy 1.19.4 버그 있음 numpy 1.19.3 사용.
"""


# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("note_pad_menu.png")
#     print("발견실패")
# pyautogui.click(file_menu_notepad)

"""
    시간 제한 설정하여 코딩.
"""


# timeout = 10
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("note_pad_menu.png")
#     end = time.time()
#     print(end, start, end - start)
#     if end - start > timeout:
#         print("시간종료")
#         sys.exit()
# pyautogui.click(file_menu_notepad)

"""
    함수로 변경
"""


def find_target(imge, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(imge)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(image, timeout=30):
    target = find_target(image, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("발견실패")
        print(f"f[Timeout {timeout}s] Target not fount ({image}).")
        sys.exit()


my_click("note_pad_menu.png", 10)
