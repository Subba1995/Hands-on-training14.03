import pyautogui
#
# print(pag.position())
brouser = pyautogui.leftClick(x=357, y=28)
pyautogui.PAUSE = 2
counter = 0
while counter <= 200:
    pyautogui.PAUSE = 6
    print(counter)
    action = pyautogui.click(x=805, y=417, clicks= 1,button="right",interval=0.5)
    counter += 1
# touch_anvil = pyautogui.click(x=1204, y=667, clicks=100, button="right", interval=0.15)
# touch_sharpening_stone =pyautogui.click(x=1572, y=652,clicks=50, button="left", interval=0.15)
# pyautogui.click(x=629, y= 378,button="right")

# chrome = pag.moveTo(326, 20),pag.click()
# music = pag.leftClick(169, 70)
# play_music = pag.leftClick(109, 1032)
# new_tab = pag.leftClick(1531, 72),pag.leftClick(1087, 118)
# youtube = pag.write("www.youtube.com", interval=0.25),pag.press("enter")




