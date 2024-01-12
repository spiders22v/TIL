# 동영상을 입력으로 받아 자동차 번호판을 검출하고 블러 처리한 후, 각 프레임에 modify_라는 접두어를 붙여 저장하는 코드

import cv2

# 동영상 파일 경로 설정
video_path = 'input_video.mp4'

# 자동차 번호판 인식을 위한 분류기 불러오기
license_plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# 동영상 파일 열기
cap = cv2.VideoCapture(video_path)

# 동영상의 속성 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 동영상 저장을 위한 VideoWriter 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = 'output_video.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# 동영상 파일이 열려있는 동안 반복
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 그레이 스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 자동차 번호판 검출
    license_plates = license_plate_cascade.detectMultiScale(gray, 1.1, 5)

    # 검출된 번호판 블러 처리
    for (x, y, w, h) in license_plates:
        license_plate_roi = frame[y:y+h, x:x+w]
        license_plate_roi = cv2.GaussianBlur(license_plate_roi, (99, 99), 0)  # 블러 처리
        frame[y:y+h, x:x+w] = license_plate_roi

    # 화면에 출력
    cv2.imshow('License Plate Blurring', frame)

    # 프레임 저장
    out.write(frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 동영상 파일과 윈도우 창 닫기
cap.release()
out.release()
cv2.destroyAllWindows()
