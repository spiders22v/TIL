# 자동차 번호판을 인식하여 블러처리 해주는 코드를 작성해줘.

import cv2
import os

# 현재 디렉토리 내 모든 파일 검색
for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 이미지 파일 불러오기
        image = cv2.imread(filename)

        # 자동차 번호판 인식을 위한 분류기 불러오기
        license_plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

        # 그레이 스케일로 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 자동차 번호판 검출
        license_plates = license_plate_cascade.detectMultiScale(gray, 1.1, 5)

        # 검출된 번호판 블러 처리
        for (x, y, w, h) in license_plates:
            # 번호판 부분을 추출하여 블러 처리
            license_plate_roi = image[y:y+h, x:x+w]
            license_plate_roi = cv2.GaussianBlur(license_plate_roi, (99, 99), 0)  # 블러 처리
            image[y:y+h, x:x+w] = license_plate_roi

        # 수정된 파일 저장
        modified_filename = 'modi_' + filename
        cv2.imwrite(modified_filename, image)
