import qrcode
import os

# 데이터가 저장된 파일 경로
file_path = os.path.join("04.QR코드 생성기", "qrdata.txt")

# QR 코드 생성 함수
def create_qrcode(data):
    # QR 코드 생성
    img = qrcode.make(data)

    # 이미지 파일로 저장
    img_file_path = os.path.join("04.QR코드 생성기", f"qrcode_{data}.png")
    img.save(img_file_path)

# qrdata.txt 파일에서 데이터 읽어오기
with open(file_path, 'r') as f:
    for line in f:
        # 개행 문자 제거
        data = line.strip()
        create_qrcode(data)
