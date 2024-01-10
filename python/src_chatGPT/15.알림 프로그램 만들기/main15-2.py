from datetime import datetime, timedelta
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    now = datetime.now()
    if now.weekday() in [0, 2, 4] and now.hour == 9 and now.minute == 50:
        # 다음 회의 시작 시간 계산
        next_meeting_time = now + timedelta(minutes=10)
        next_meeting_time_str = next_meeting_time.strftime("%Y-%m-%d %H:%M:%S")

        # 알림 표시
        toaster.show_toast("알림", f"{next_meeting_time_str}에 회의가 시작됩니다.", duration=10)

    # 1초마다 반복
    time.sleep(1)
