# 파이썬으로 패스워드 생성하는 GUI 프로그램을 만들어줘. 몇 가지 조건이 있어. 1) 패스워드의 길이를 설정할 수 있어야 해. 2) 포함하는 특수문자를 입력할 수 있어야해. 3) 생성된 패스워드는 바로 보여줘. 4) GUI의 크기는 가로300 세로 200픽셀로 해줘.


import random
import string
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QVBoxLayout

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # 기본값 설정
        self.password_length = 12
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_numbers = True
        self.include_special_characters = True

        # UI 구성
        self.title_label = QLabel("패스워드 생성기")
        self.password_label = QLabel("생성된 패스워드: ")
        self.password_textbox = QLineEdit()
        self.length_label = QLabel("패스워드 길이: ")
        self.length_textbox = QLineEdit(str(self.password_length))
        self.uppercase_checkbox = QCheckBox("대문자 포함")
        self.uppercase_checkbox.setChecked(self.include_uppercase)
        self.lowercase_checkbox = QCheckBox("소문자 포함")
        self.lowercase_checkbox.setChecked(self.include_lowercase)
        self.numbers_checkbox = QCheckBox("숫자 포함")
        self.numbers_checkbox.setChecked(self.include_numbers)
        self.special_checkbox = QCheckBox("특수문자 포함")
        self.special_checkbox.setChecked(self.include_special_characters)
        self.generate_button = QPushButton("패스워드 생성")

        # UI 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_textbox)
        vbox.addWidget(self.length_label)
        vbox.addWidget(self.length_textbox)
        vbox.addWidget(self.uppercase_checkbox)
        vbox.addWidget(self.lowercase_checkbox)
        vbox.addWidget(self.numbers_checkbox)
        vbox.addWidget(self.special_checkbox)
        vbox.addWidget(self.generate_button)
        self.setLayout(vbox)

        # 이벤트 처리 함수 등록
        self.generate_button.clicked.connect(self.generate_password)
        self.length_textbox.textChanged.connect(self.update_length)
        self.uppercase_checkbox.stateChanged.connect(self.update_uppercase)
        self.lowercase_checkbox.stateChanged.connect(self.update_lowercase)
        self.numbers_checkbox.stateChanged.connect(self.update_numbers)
        self.special_checkbox.stateChanged.connect(self.update_special)

        # 초기 패스워드 생성
        self.generate_password()

        # 윈도우 설정
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("패스워드 생성기")
        self.show()

    def generate_password(self):
        # 사용자 설정에 따른 패스워드 생성
        characters = ''
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_lowercase:
            characters += string.ascii_lowercase
        if self.include_numbers:
            characters += string.digits
        if self.include_special_characters:
            characters += string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.password_length))
        self.password_textbox.setText(password)

    def update_length(self, text):
        # 패스워드 길이 변경
        try:
            self.password_length = int(text)
            self.generate_password()
        except ValueError:
            pass

    def update_uppercase(self, state):
        # 대문자 포함 여부 변경
        self.include_uppercase = bool(state)
        self.generate_password()

    def update_lowercase(self, state):
        # 소문자 포함 여부 변경
        self.include_lowercase = bool(state)
        self.generate_password()

    def update_numbers(self, state):
        # 숫자 포함 여부 변경
        self.include_numbers = bool(state)
        self.generate_password()

    def update_special(self, state):
        # 특수문자 포함 여부 변경
        self.include_special_characters = bool(state)
        self.generate_password()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())

