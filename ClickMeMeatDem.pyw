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
pyautogui.doubleClick(x=539, y=248) #clciks bar


pyautogui.write('1000891', interval=.25) #makes ribeyes
pyautogui.press('enter')

time.sleep (5)
pyautogui.click(x=563, y=391)#clicks fresh
time.sleep (5)
#make a loop here
a=1
b=6000
for n in range(100):
    string = str(a)
    pyautogui.click(x=816, y=391) #print
    time.sleep (5)
    pyautogui.click(x=628, y=632) #click bar
    time.sleep (5)
    pyautogui.write('100', interval=.25) #inputs weight
    time.sleep (10)
    pyautogui.click(x=798, y=467) #click ok
    time.sleep (10)
    pyautogui.click(x=266, y=427) #click name bar
    time.sleep (15)
    pyautogui.write(string, interval=.25)#names file
    time.sleep (15)
    pyautogui.click(x=455, y=499) #saves
    time.sleep (15)
    a=a+1


pyautogui.doubleClick(x=539, y=248) #clciks bar
pyautogui.write('1000890', interval=.25) #makes carcuss
pyautogui.press('enter')
time.sleep (15)
#make a loop here

for p in range(100):
    
    mstring = str(b)
    pyautogui.click(x=816, y=391) #click print
    time.sleep (10)
    pyautogui.click(x=628, y=632)#chick bar
    time.sleep (10)
    pyautogui.write('600', interval=.25) #weight
    time.sleep (10)
    pyautogui.click(x=798, y=467) #Enter
    time.sleep (10)
    pyautogui.click(x=464, y=427) #pdfname
    time.sleep (10)
    pyautogui.write(mstring, interval=.25)#names file
    time.sleep (10)
    pyautogui.click(x=455, y=499) #saves
    time.sleep (10)
    b=b+1


