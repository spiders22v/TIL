# 윈도우의 알림을 출력하는  프로그램 만들어줘. 

from win10toast import ToastNotifier

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

if __name__ == "__main__":
    # 사용자로부터 알림 제목과 메시지 입력 받기
    notification_title = input("알림 제목을 입력하세요: ")
    notification_message = input("알림 메시지를 입력하세요: ")

    # 알림 출력
    show_notification(notification_title, notification_message)
