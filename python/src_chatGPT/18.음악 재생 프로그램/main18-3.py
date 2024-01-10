import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")
        # 음악 파일 경로
        self.file = None
        
        # 초기화
        pygame.init()

        # UI 구성
        self.label = tk.Label(self.root, text="Music Player")
        self.label.pack(pady=10)

        self.file_button = tk.Button(self.root, text="Choose File", command=self.choose_file)
        self.file_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, state="disabled")
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, state="disabled")
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, state="disabled")
        self.stop_button.pack(pady=5)

    def choose_file(self):
        # 파일 대화상자 열기
        self.file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=[("Audio Files", "*.mp3;*.wav")])

        # 파일 선택 후 버튼 활성화
        if self.file:
            self.play_button.config(state="normal")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")

    def play_music(self):
        # 음악 파일 로드
        pygame.mixer.music.load(self.file)
        
        # 재생
        pygame.mixer.music.play()

    def pause_music(self):
        # 일시정지
        pygame.mixer.music.pause()

    def stop_music(self):
        # 정지
        pygame.mixer.music.stop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

    # 종료
    pygame.quit()
