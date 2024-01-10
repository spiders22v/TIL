# 파이썬으로 CPU, RAM, 네트워크의 사용량을 1초마다 출력하는 프로그램을 작성해줘. 

import psutil
import time

def print_system_stats():
    try:
        while True:
            # CPU 사용량 및 코어 수 출력
            cpu_percent = psutil.cpu_percent()
            cpu_cores = psutil.cpu_count(logical=False)
            print(f"CPU 사용량: {cpu_percent}% (코어 수: {cpu_cores})")

            # RAM 사용량 출력
            ram_percent = psutil.virtual_memory().percent
            print(f"RAM 사용량: {ram_percent}%")

            # 네트워크 사용량 출력
            network_stats = psutil.net_io_counters()
            print(f"네트워크 수신: {network_stats.bytes_recv} bytes, 전송: {network_stats.bytes_sent} bytes")

            print("-" * 30)
            time.sleep(1)  # 1초 대기
    except KeyboardInterrupt:
        print("프로그램이 종료되었습니다.")

if __name__ == "__main__":
    print_system_stats()
