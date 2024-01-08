import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect(r'25.가상화폐 데이터 획득하여 데이터베이스에 저장\upbit.db')
cur = conn.cursor()

# BTC-KRW 가격 조회
cur.execute("SELECT * FROM BTC_KRW")
rows = cur.fetchall()

# 조회 결과 출력
for row in rows:
    print(row)

# 연결 종료
conn.close()
