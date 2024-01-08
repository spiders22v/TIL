# 사용자에게 데이터를 입력받고, 해당 데이터를 포함하는 QR 코드를 생성하여 지정한 파일명으로 저장하는 파이썬 코드 작성해줘.

import qrcode

def generate_qr_code(data, file_name='qrcode.png'):
    try:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # QR 코드 이미지 생성
        img = qr.make_image(fill_color="black", back_color="white")

        # 이미지를 파일로 저장
        img.save(file_name)
        print(f"QR 코드가 {file_name} 파일로 저장되었습니다.")
    except Exception as e:
        print(f"QR 코드 생성 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    data_to_encode = input("QR 코드로 변환할 데이터를 입력하세요: ")
    file_name = input("저장할 파일명을 입력하세요 (기본값: qrcode.png): ") or 'qrcode.png'
    generate_qr_code(data_to_encode, file_name=file_name)