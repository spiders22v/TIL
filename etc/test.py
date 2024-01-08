import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QTextEdit

class DockerfileGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # GUI 요소 생성
        self.label_base_image = QLabel('베이스 이미지:')
        self.combo_base_image = QComboBox()
        self.combo_base_image.addItems(['파이토치', '텐서플로우'])

        self.label_code = QLabel('사용자 파이썬 코드:')
        self.text_code = QTextEdit()

        self.label_output = QLabel('도커파일 내용:')
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.btn_generate = QPushButton('도커파일 생성')
        self.btn_generate.clicked.connect(self.generate_dockerfile)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label_base_image)
        layout.addWidget(self.combo_base_image)
        layout.addWidget(self.label_code)
        layout.addWidget(self.text_code)
        layout.addWidget(self.label_output)
        layout.addWidget(self.output_text)
        layout.addWidget(self.btn_generate)

        self.setLayout(layout)

        # 윈도우 설정
        self.setWindowTitle('Dockerfile Generator')
        self.setGeometry(300, 300, 400, 300)

    def generate_dockerfile(self):
        # 사용자 입력 가져오기
        base_image = self.combo_base_image.currentText().lower()
        user_code = self.text_code.toPlainText().strip()

        # 도커파일 생성
        dockerfile_content = f"FROM {base_image}\n\n"\
                             f"# 사용자 코드 추가\n"\
                             f"RUN mkdir /app\n"\
                             f"WORKDIR /app\n"\
                             f"RUN echo '{user_code}' > user_code.py\n\n"\
                             f"# 필요한 라이브러리 설치\n"\
                             f"COPY requirements.txt ./\n"\
                             f"RUN pip install --no-cache-dir -r requirements.txt\n\n"\
                             f"# 실행 명령어\n"\
                             f"CMD [\"python\", \"user_code.py\"]"

        # 결과 텍스트에 표시
        self.output_text.setPlainText(dockerfile_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockerfileGenerator()
    window.show()
    sys.exit(app.exec_())
