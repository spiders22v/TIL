# 파이썬으로 월요일, 수요일, 금요일 9시 50분에 "회의시작 10분전 입니다."의 알림을 표시하는 프로그램 작성해줘.

import schedule
import time
from win10toast import ToastNotifier
from datetime import datetime, timedelta

def show_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("알림", message, duration=10)

def job():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"회의 시작 10분 전입니다. (현재 시간: {current_time})"
    show_notification(message)

# 특정 시간에 작업 예약
schedule.every().monday.at("09:50").do(job)
schedule.every().wednesday.at("09:50").do(job)
schedule.every().friday.at("09:50").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# 주의: 이 코드는 무한 루프로 계속 실행되므로 종료하려면 수동으로 종료해야 합니다. 