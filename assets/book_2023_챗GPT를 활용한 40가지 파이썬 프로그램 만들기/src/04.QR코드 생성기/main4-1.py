import qrcode

# QR 코드에 넣을 데이터
data = "Hello, World!"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장
img.save("qrcode.png")