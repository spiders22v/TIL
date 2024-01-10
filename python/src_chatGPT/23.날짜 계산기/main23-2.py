import datetime

print("기준 날짜부터 오늘까지 몇일이 지났는지 계산하는 프로그램입니다.")
print("연도, 월, 일을 차례로 입력하세요.")
year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))

start_date = datetime.date(year, month, day)
end_date = datetime.date.today()

days_diff = (end_date - start_date).days

print(start_date.strftime("%Y년 %m월 %d일"), "부터 오늘까지", days_diff, "일이 지났습니다.")
