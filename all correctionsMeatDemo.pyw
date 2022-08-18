import pyautogui
import time
#set resolution to 1290 x 960

pyautogui.doubleClick(x=32, y=627) #open
time.sleep (10)
pyautogui.doubleClick(x=32, y=724) #open
time.sleep (10)
pyautogui.doubleClick(x=635, y=496) #closes popup
time.sleep (10)
pyautogui.doubleClick(x=32, y=825) #opens production
time.sleep (10)

a=3007541
for n in range(229):
    
    pyautogui.click(x=1212, y=117) #clciks more
    time.sleep (10)
    pyautogui.click(x=556, y=394) #clciks correct
    time.sleep (10)
    pyautogui.click(x=725, y=623) #clciks bar
    time.sleep (10)
    pyautogui.write(str(a), interval=.25) #inputs van
    time.sleep (10)
    pyautogui.click(x=807, y=466) #clciks okay
    time.sleep (10)
    pyautogui.click(x=817, y=364) #clciks print
    time.sleep (10)
    pyautogui.click(x=674, y=620) #clciks bar
    time.sleep (10)
    pyautogui.write("890", interval=.25) #inputs weight
    time.sleep (10)
    pyautogui.click(x=790, y=465) #clciks okay
    time.sleep (10)
    pyautogui.click(x=182, y=425) #clciks namebar
    time.sleep (10)
    pyautogui.write(str(a), interval=.25) #inputs van
    time.sleep (10)
    pyautogui.click(x=448, y=497) #clciks save
    time.sleep (10)
    a = a+1
