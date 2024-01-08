# 파이썬으로 컴퓨터 외부의 IP를 확인하는 코드를 작성해줘. 

import requests

def get_external_ip():
    try:
        # 외부 서비스를 사용하여 외부 IP 주소 가져오기
        response = requests.get("https://api64.ipify.org?format=json")
        # 외부 서비스의 응답을 JSON 형식으로 해석하여 외부 IP 주소 추출
        external_ip = response.json()["ip"]
        return external_ip
    except requests.RequestException as e:
        # 요청 중 오류가 발생하면 오류 메시지를 출력하고 None 반환
        print(f"외부 IP 주소를 가져오는 중 오류가 발생했습니다: {e}")
        return None

if __name__ == "__main__":
    # get_external_ip 함수 호출하여 외부 IP 주소 가져오기
    external_ip = get_external_ip()

    # 가져온 외부 IP 주소 출력
    if external_ip:
        print(f"외부 IP 주소: {external_ip}")
    else:
        print("외부 IP 주소를 가져오는 데 실패했습니다.")
