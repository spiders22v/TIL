import datetime

print("날짜 계산기 프로그램입니다.")
print("연도, 월, 일을 차례로 입력하세요.")
year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))

given_date = datetime.date(year, month, day)

print("입력한 날짜는", given_date.strftime("%Y년 %m월 %d일"), "입니다.")
print("이 날짜에서 몇 일을 더하거나 빼시겠습니까?")
days_diff = int(input("일 수: "))

result_date = given_date + datetime.timedelta(days=days_diff)

print(days_diff, "일을 더하거나 빼면", result_date.strftime("%Y년 %m월 %d일"), "입니다.")
