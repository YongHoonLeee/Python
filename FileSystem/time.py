import time
import datetime

now = datetime.datetime.now()
print(now)
# 주차를 말한다. 현재는 2020년도의 8주차 3은 요일 일:0 월:1 ... 이라서 오늘 수요일이라 3 신기.
print(now.isocalendar())
print(now.isoformat())
print(now.strftime('%y_%m_%d'))
print("#######")

today = datetime.date.today()
print(today)

d= datetime.timedelta(weeks=1)
print('일주일후 :',now+d)
print('일주일전 :',now-d)
yd = datetime.timedelta(days=365)
print('1 years age :',now-yd)
print('1 years after :',now+yd)

for i in range(5):
    print(i)
    time.sleep(1) # 초단위로 가만히 있는거.

#Data Back-up by timeData
import os
import shutil

# if os.path.exists('time.py'):
#     shutil.copy('time.py',"{}.{}".format('time.py',now))
# 위에꺼 잘 됬는지를 모르겟네.

