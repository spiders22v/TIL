import pygame

# 음악 파일 경로 설정
file = r'18.음악 재생 프로그램\1번 안녕하세요.mp3'

# 초기화
pygame.init()

# 음악 파일 로드
pygame.mixer.music.load(file)

# 재생
pygame.mixer.music.play()

# 재생이 끝날 때까지 대기
while pygame.mixer.music.get_busy():
    continue

# 종료
pygame.quit()
