import requests

response = requests.get('https://ipinfo.io/ip')
external_ip = response.text.strip()

print("외부 IP: " + external_ip)