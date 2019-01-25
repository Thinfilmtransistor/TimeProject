import time
from datetime import datetime
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while True:
    minute = int(datetime.utcnow().strftime('%M'))
    second = float(datetime.utcnow().strftime('%S.%f'))
    if minute == 23:
        print("before",minute, second)
        # time.sleep(0.5) # 0.673 ~ 0.6735
        # time.sleep(0.673) # 0.673 ~ 0.6735
        click(1880, 960)
        break
    else:
        print(second)

minute = int(datetime.utcnow().strftime('%M'))
second = float(datetime.utcnow().strftime('%S.%f'))
print("after",minute, second)
now = str(datetime.now())
f = open('C:/Python/project/MakeLog.txt', "a")
f.write("\n"+now)

f.close()

