import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 데이터베이스 파일에 연결
conn = sqlite3.connect(r'26.데이터베이스의 데이터 읽어 그래프 그리기\upbit.db')

# 쿼리문 작성
query = 'SELECT * FROM BTC_KRW'

# 데이터 가져오기
cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()

# 날짜와 금액을 분리하여 리스트에 저장
dates = [row[0] for row in rows]
amounts = [row[1] for row in rows]

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot_date(dates, amounts, '-')
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Upbit Data')
plt.show()

# 연결 종료
conn.close()
