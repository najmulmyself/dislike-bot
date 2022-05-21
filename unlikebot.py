import pyautogui
import pyperclip
import time


while True:
    time.sleep(3)
    pyautogui.hotkey('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    # pyautogui.press('tab')
    time.sleep(1)
    # pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('esc')
    # url = pyautogui.hotkey('ctrl', 'v')
    url = str(pyperclip.paste())
    time.sleep(1)
    print(url)
    kaniz = '@prity'
    if kaniz in url:
        pyautogui.press('down')
    else: 
        pyautogui.press('l')
        time.sleep(2)
        pyautogui.press('down')