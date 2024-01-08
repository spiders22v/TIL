import psutil  # psutil 모듈을 사용하기 위해 import 합니다.
import time   # time 모듈을 사용하기 위해 import 합니다.

# 무한루프를 돌며 CPU, RAM, 네트워크 사용량을 출력합니다.
while True:
    # CPU 사용량을 구하고 출력합니다.
    cpu_percent = psutil.cpu_percent(interval=None)
    print(f"CPU 사용량: {cpu_percent}%")

    # 메모리 사용량을 구하고 출력합니다.
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    print(f"메모리 사용량: {mem_percent}%")

    # 네트워크 사용량을 구하고 출력합니다.
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    print(f"네트워크 사용량: 송신={bytes_sent}bytes, 수신={bytes_recv}bytes")

    # 1초 대기합니다.
    time.sleep(1)
