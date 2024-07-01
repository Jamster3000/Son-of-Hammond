import time
import pyautogui

SHORT_BREAK = 0.37
MEDIUM_BREAK = 1.7
LONG_BREAK = 5

def start_timer():
    print("================")
    print("=== STARTING ===")
    print("================")
    pyautogui.hotkey("0", "x")
    time.sleep(2)
    print("RECORDING")
    pyautogui.hotkey("ctrl", "shift", "S")

def intro():
    pyautogui.hotkey("0", "2")
    time.sleep(MEDIUM_BREAK)
    pyautogui.hotkey("0", "4")
    time.sleep(MEDIUM_BREAK)
    pyautogui.hotkey("1", "3")
    time.sleep(MEDIUM_BREAK-0.8)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(MEDIUM_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(MEDIUM_BREAK)
    pyautogui.hotkey("1", "3")
    time.sleep(MEDIUM_BREAK)
    pyautogui.hotkey("0", "2", "4")
    time.sleep(MEDIUM_BREAK+0.65)
    
def main():
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")

###########################################

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("2", "4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    
######################################    

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
#######################################

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("2", "4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(MEDIUM_BREAK)
    
def bridge():
    pyautogui.press("8")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)

    pyautogui.press("7")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    
    pyautogui.press("8")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("0")
    time.sleep(SHORT_BREAK)

    pyautogui.press("7")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    
#####################################

    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("0")
    time.sleep(SHORT_BREAK)

    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("0")
    time.sleep(SHORT_BREAK)
    
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)

    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)

#################################

    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("0")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)

    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    
    pyautogui.press("0")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)

    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    time.sleep(SHORT_BREAK)
    
def second_main():
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")

###########################################

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("2", "4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    
######################################    

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
#######################################

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("2", "4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)

def outro():
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")

###########################################

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("2", "4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    time.sleep(SHORT_BREAK)
    pyautogui.press("8")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("7")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    
######################################    

    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("2")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    
    time.sleep(SHORT_BREAK)
    pyautogui.hotkey("0", "2")
    time.sleep(SHORT_BREAK)
    pyautogui.press("4")
    time.sleep(SHORT_BREAK)
    pyautogui.press("6")
    
    time.sleep(SHORT_BREAK)
    pyautogui.press("1")
    time.sleep(SHORT_BREAK)
    pyautogui.press("3")
    time.sleep(SHORT_BREAK)
    pyautogui.press("5")
    time.sleep(SHORT_BREAK+0.3)
    pyautogui.hotkey("4", "0")
    

start_timer()
intro()
main()
bridge()
second_main()
outro()

time.sleep(5)

pyautogui.hotkey("ctrl", "shift", "X")