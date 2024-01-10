# 파이썬으로 QR코드를 생성하는 코드를 작성해줘. 이미지 파일이 저장되는 위치는 하위 폴더를 검색하여 04.QR코드 생성기 폴더에 저장되게끔 작성해줘.

import qrcode
import os

def generate_qr_code(data, file_name='qrcode.png', target_folder='04.QR코드 생성기'):
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

        # 하위 폴더를 검색하여 04.QR코드 생성기 폴더에 이미지 파일 저장
        for root, dirs, files in os.walk(os.getcwd()):
            if target_folder in dirs:
                file_path = os.path.join(root, target_folder, file_name)
                img.save(file_path)
                print(f"QR 코드가 {file_path} 파일로 저장되었습니다.")
                return

        # 04.QR코드 생성기 폴더를 찾지 못한 경우 경고 출력
        print(f"'{target_folder}' 폴더를 찾을 수 없어 QR 코드를 저장할 수 없습니다.")
    except Exception as e:
        print(f"QR 코드 생성 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    data_to_encode = input("QR 코드로 변환할 데이터를 입력하세요: ")
    file_name = input("저장할 파일명을 입력하세요 (기본값: qrcode.png): ") or 'qrcode.png'
    generate_qr_code(data_to_encode, file_name=file_name)
