import tkinter as tk
import vlc

# 라디오 방송 정보
radios = {
    'EBS FM': 'http://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8',
    'EBS 책읽어주는 라디오': 'http://fmbook.ebs.co.kr/fmbook/live_m4a/playlist.m3u8',
    'EBS 외국어1': 'http://new_iradio.ebs.co.kr/iradio/iradiolive_m4a/playlist.m3u8',
    'EBS 외국어2': 'http://bandibook.ebs.co.kr/bandibook/live_m4a/playlist.m3u8',
    'TBS FM 교통방송': 'http://tbs.hscdn.com/tbsradio/fm/playlist.m3u8',
    'TBS eFM': 'http://tbs.hscdn.com/tbsradio/efm/playlist.m3u8',
}

class RadioPlayer:
    def __init__(self, master):
        self.master = master
        master.title('라디오')
        master.geometry('200x100')
        # 라디오 선택 메뉴 생성
        self.radio_var = tk.StringVar(master)
        self.radio_var.set(list(radios.keys())[0])
        self.radio_menu = tk.OptionMenu(master, self.radio_var, *radios.keys())
        self.radio_menu.pack()
        
        # 재생/일시정지/중지 버튼 생성
        self.play_button = tk.Button(master, text='재생', command=self.play_radio)
        self.pause_button = tk.Button(master, text='일시정지', command=self.pause_radio)
        self.stop_button = tk.Button(master, text='중지', command=self.stop_radio)
        self.play_button.pack(side=tk.LEFT, padx=10)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        # 미디어 재생을 위한 인스턴스 생성
        self.instance = vlc.Instance('--no-xlib')
        
        # 미디어 플레이어 생성
        self.media_player = self.instance.media_player_new()
        
        # 초기 상태
        self.is_playing = False
    
    def play_radio(self):
        """선택한 라디오 방송을 재생합니다."""
        radio_url = radios[self.radio_var.get()]
        media = self.instance.media_new(radio_url)
        self.media_player.set_media(media)
        self.media_player.play()
        self.is_playing = True
        
    def pause_radio(self):
        """현재 재생 중인 라디오 방송을 일시정지합니다."""
        if self.is_playing:
            self.media_player.pause()
            self.is_playing = False
        
    def stop_radio(self):
        """현재 재생 중인 라디오 방송을 중지합니다."""
        if self.is_playing:
            self.media_player.stop()
            self.is_playing = False

root = tk.Tk()
radio_player = RadioPlayer(root)
root.mainloop()