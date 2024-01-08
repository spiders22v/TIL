# 파이썬으로 컴퓨터 내부의 IP를 확인하는 코드를 작성해줘. 

import socket

def get_internal_ip():
    try:
        # 호스트 이름을 사용하여 내부 IP 주소 가져오기
        internal_ip = socket.gethostbyname(socket.gethostname())
        return internal_ip
    except socket.error as e:
        print(f"내부 IP 주소를 가져오는 중 오류가 발생했습니다: {e}")
        return None

if __name__ == "__main__":
    internal_ip = get_internal_ip()

    if internal_ip:
        print(f"내부 IP 주소: {internal_ip}")
    else:
        print("내부 IP 주소를 가져오는 데 실패했습니다.")