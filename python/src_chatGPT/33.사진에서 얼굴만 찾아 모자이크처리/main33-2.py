import cv2
import numpy as np

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 현재 디렉토리 내 모든 파일 검색
for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 이미지 파일 불러오기
        image = cv2.imread(filename)

        # 얼굴 인식을 위한 분류기 불러오기
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # 그레이 스케일로 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 얼굴 검출
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # 검출된 얼굴 모자이크 처리
        for (x, y, w, h) in faces:
            # 얼굴 부분을 추출하여 모자이크 처리
            face_roi = image[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (50, 50))
            face_roi = cv2.resize(face_roi, (w, h), interpolation=cv2.INTER_AREA)
            image[y:y+h, x:x+w] = face_roi

        # 수정된 파일 저장
        modified_filename = 'modify_' + filename
        cv2.imwrite(modified_filename, image)
