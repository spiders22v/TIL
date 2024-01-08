import vlc

# 미디어 재생을 위한 인스턴스 생성
player = vlc.Instance('--no-xlib')

# 재생할 미디어의 URL
url = 'http://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8'

# 미디어 플레이어 생성
media_player = player.media_player_new()

# 미디어 재생을 위한 미디어 생성
media = player.media_new(url)

# 미디어 플레이어에 미디어 설정
media_player.set_media(media)

# 미디어 재생
media_player.play()

# 재생이 종료될 때까지 대기
while True:
    pass
