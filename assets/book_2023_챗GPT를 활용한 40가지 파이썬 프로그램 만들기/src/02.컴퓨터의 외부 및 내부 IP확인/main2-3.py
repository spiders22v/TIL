import socket
import requests

# 내부 IP 가져오기
hostname = socket.gethostname()
internal_ip = socket.gethostbyname(hostname)

# 외부 IP 가져오기
response = requests.get('https://ipinfo.io/ip')
external_ip = response.text.strip()

# 출력
print("내부 IP:", internal_ip)
print("외부 IP:", external_ip)
