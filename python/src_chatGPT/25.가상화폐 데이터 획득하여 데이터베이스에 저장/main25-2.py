import pyupbit
import sqlite3
import datetime
import time

# 데이터베이스 연결
conn = sqlite3.connect(r'25.가상화폐 데이터 획득하여 데이터베이스에 저장\upbit.db')
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW (time TEXT, price INTEGER)")

# 10초마다 시세 조회 및 데이터베이스에 저장
while True:
    try:
        price = pyupbit.get_current_price("KRW-BTC")
        now = datetime.datetime.now()

        # 조회 결과 출력
        print(now, price)

        # 데이터베이스에 저장
        cur.execute("INSERT INTO BTC_KRW (time, price) VALUES (?, ?)", (now, price))
        conn.commit()

        # 10초 대기
        time.sleep(10)

    except Exception as e:
        print(e)
        time.sleep(1)

# 연결 종료
conn.close()
