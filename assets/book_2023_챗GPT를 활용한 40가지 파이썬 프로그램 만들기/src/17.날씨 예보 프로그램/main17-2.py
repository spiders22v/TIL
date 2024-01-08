import requests
import json
import datetime
import openpyxl
import time

api_key = '58659c9f71f5c4b54841fc18d52d990a'  # 여기에 발급받은 API 키를 입력하세요.
city_name = 'seoul'

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Date', 'Time', 'Weather', 'Temperature', 'Feels Like'])

while True:
    # API 호출
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)

    # JSON 데이터 파싱
    data = json.loads(response.text)

    # 날씨 정보 저장
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']

    # 엑셀 파일에 데이터 추가
    ws.append([current_time.split()[0], current_time.split()[1], weather, temp, feels_like])
    wb.save(r'17.날씨 예보 프로그램\날씨저장.xlsx')

    # 30분 대기
    time.sleep(1800)
