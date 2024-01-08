# 파이썬으로 컴퓨터 내부 및 외부 IP를 한꺼번에 출력하는 코드를 작성해줘.

import socket
import requests

def get_internal_ip():
    try:
        # 호스트 이름을 사용하여 내부 IP 주소 가져오기
        internal_ip = socket.gethostbyname(socket.gethostname())
        return internal_ip
    except socket.error as e:
        # 소켓 에러가 발생하면 내부 IP 주소를 가져오는 데 실패한 것으로 간주
        print(f"내부 IP 주소를 가져오는 중 오류가 발생했습니다: {e}")
        return None

def get_external_ip():
    try:
        # httpbin.org 서비스를 사용하여 외부 IP 주소 가져오기
        response = requests.get("https://httpbin.org/ip")
        # 외부 서비스의 응답을 JSON 형식으로 해석하여 외부 IP 주소 추출
        external_ip = response.json()["origin"]
        return external_ip
    except requests.RequestException as e:
        # 요청 중 오류가 발생하면 외부 IP 주소를 가져오는 데 실패한 것으로 간주
        print(f"외부 IP 주소를 가져오는 중 오류가 발생했습니다: {e}")
        return None

if __name__ == "__main__":
    # 내부 IP 주소 가져오기
    internal_ip = get_internal_ip()
    if internal_ip:
        print(f"내부 IP 주소: {internal_ip}")
    else:
        print("내부 IP 주소를 가져오는 데 실패했습니다.")

    # 외부 IP 주소 가져오기
    external_ip = get_external_ip()
    if external_ip:
        print(f"외부 IP 주소: {external_ip}")
    else:
        print("외부 IP 주소를 가져오는 데 실패했습니다.")
