import time
from datetime import datetime
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


print(time.time())
print(time.ctime())
print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))

# print(time.strftime("%H:%M:%S.%f",time.localtime()))
# print(time.clock_gettime_ns())

while True:
    minute = int(datetime.utcnow().strftime('%M'))
    second = float(datetime.utcnow().strftime('%S.%f'))
    if minute == 0:
        print("before",minute, second)
        time.sleep(0.6729) # 0.673 ~ 0.6735
        # time.sleep(0.673) # 0.673 ~ 0.6735
        click(1880, 960)

        minute = int(datetime.utcnow().strftime('%M'))
        second = float(datetime.utcnow().strftime('%S.%f'))
        print("after",minute, second)
        break
    else:
        print(second)
