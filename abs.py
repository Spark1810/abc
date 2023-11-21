import time
import pyautogui

def openapp(sv):
    # Press the Windows key
    pyautogui.press('win')

    # Wait for the Start menu to open (you may need to adjust the duration)
    time.sleep(1)

    # Type "calculator"
    pyautogui.typewrite(sv)

    # Wait for search results (you may need to adjust the duration)
    time.sleep(1)

    # Press Enter
    pyautogui.press('enter')

sv = st.text_input("Enter the Application name:")
openapp(sv)
