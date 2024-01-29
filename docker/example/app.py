import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QFileDialog
from PyQt5.QtCore import Qt
import subprocess

class DockerConfigApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Docker Image Configurator')

        self.ubuntu_version_label = QLabel('Ubuntu Version (e.g., 22.04):', self)
        self.ubuntu_version_input = QLineEdit(self)
        self.image_name_label = QLabel('Docker Image Name:', self)
        self.image_name_input = QLineEdit(self)
        self.dockerfile_label = QLabel('Path to Dockerfile:', self)
        self.dockerfile_input = QLineEdit(self)
        self.dockerfile_input.setText('Dockerfile')  # 현재 경로에 Dockerfile이 생성될 것으로 가정
        self.dockerfile_button = QPushButton('Browse', self)
        self.torch_version_label = QLabel('PyTorch Version:', self)
        self.torch_version_combobox = QComboBox(self)
        self.torch_version_combobox.addItems(['설치하지 않음', '1.9.0', '1.8.0', '1.7.1'])  # 버전 리스트
        self.tf_version_label = QLabel('TensorFlow Version:', self)
        self.tf_version_combobox = QComboBox(self)
        self.tf_version_combobox.addItems(['설치하지 않음', '2.7.0', '2.6.0', '2.5.0'])  # 버전 리스트
        self.config_output_label = QLabel('Output Image Name:', self)
        self.config_output_input = QLineEdit(self)
        self.config_output_input.setPlaceholderText('Optional: Defaults to Image Name')
        self.config_output_input.setToolTip('Optional: Defaults to Image Name')
        self.config_output_input.setAlignment(Qt.AlignCenter)
        self.build_button = QPushButton('Build Docker Image', self)
        self.show_dockerfile_button = QPushButton('Show Dockerfile', self)
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.dockerfile_text = QTextEdit(self)
        self.dockerfile_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.ubuntu_version_label)
        layout.addWidget(self.ubuntu_version_input)
        layout.addWidget(self.image_name_label)
        layout.addWidget(self.image_name_input)
        layout.addWidget(self.dockerfile_label)
        layout.addWidget(self.dockerfile_input)
        layout.addWidget(self.dockerfile_button)
        layout.addWidget(self.torch_version_label)
        layout.addWidget(self.torch_version_combobox)
        layout.addWidget(self.tf_version_label)
        layout.addWidget(self.tf_version_combobox)
        layout.addWidget(self.config_output_label)
        layout.addWidget(self.config_output_input)
        layout.addWidget(self.build_button)
        layout.addWidget(self.show_dockerfile_button)
        layout.addWidget(self.output_text)
        layout.addWidget(self.dockerfile_text)

        self.build_button.clicked.connect(self.on_build)
        self.show_dockerfile_button.clicked.connect(self.show_dockerfile)
        self.dockerfile_button.clicked.connect(self.browse_dockerfile)

        self.setLayout(layout)

    def on_build(self):
        ubuntu_version = self.ubuntu_version_input.text()
        image_name = self.image_name_input.text()
        dockerfile_path = self.dockerfile_input.text()
        torch_version_text = self.torch_version_combobox.currentText()
        torch_version = None if torch_version_text == '설치하지 않음' else torch_version_text
        tf_version_text = self.tf_version_combobox.currentText()
        tf_version = None if tf_version_text == '설치하지 않음' else tf_version_text
        output_image_name = self.config_output_input.text() or image_name

        # Dockerfile 템플릿 생성
        dockerfile_template = f'''
# 베이스 이미지로 Ubuntu {ubuntu_version} 사용
FROM ubuntu:{ubuntu_version}

# 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive

# 기본 패키지 설치
RUN apt-get update && apt-get install -y \\
    build-essential \\
    cmake \\
    git \\
    wget \\
    vim \\
    python3 \\
    python3-pip \\
    qt5-default \\
    libqt5widgets5

# 사용자 입력에 따라 선택적으로 파이토치 설치
'''
        if torch_version:
            dockerfile_template += f'RUN pip3 install torch=={torch_version}+cpu torchvision=={torch_version}+cpu torchaudio=={torch_version}+cpu -f https://download.pytorch.org/whl/cpu.html\n'

        # 사용자 입력에 따라 선택적으로 텐서플로우 설치
        if tf_version:
            dockerfile_template += f'RUN pip3 install tensorflow=={tf_version}\n'

        # PyQt5 설치
        dockerfile_template += 'RUN pip3 install PyQt5\n'

        # 작업 디렉토리 설정
        dockerfile_template += 'WORKDIR /app\n'

        # 사용자로부터 입력 받을 설정 파일 및 도커파일 복사
        dockerfile_template += 'COPY configure_docker_image.py .\n'
        dockerfile_template += f'COPY {dockerfile_path} .\n'  # Dockerfile 경로 추가

        # 컨테이너 실행 시 실행될 명령
        dockerfile_template += 'CMD ["python3", "configure_docker_image.py"]\n'

        # Dockerfile 저장
        with open(dockerfile_path, 'w') as dockerfile:
            dockerfile.write(dockerfile_template)

        # Dockerfile 텍스트에 표시
        self.dockerfile_text.setPlainText(dockerfile_template)

        # docker build 명령어 실행
        command = f'docker build -t {output_image_name} -f {dockerfile_path} .'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # 결과 출력
        result_text = f"Command: {command}\n\nOutput:\n{output.decode('utf-8')}\nError:\n{error.decode('utf-8')}"
        self.output_text.setPlainText(result_text)

    def show_dockerfile(self):
        # 사용자가 입력한 Dockerfile 텍스트를 표시
        with open(self.dockerfile_input.text(), 'r') as dockerfile:
            dockerfile_content = dockerfile.read()

        self.dockerfile_text.setPlainText(dockerfile_content)

    def browse_dockerfile(self):
        # 사용자에게 Dockerfile 경로를 선택하도록 함
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setDefaultSuffix("Dockerfile")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.selectFile("Dockerfile")
        file_path, _ = file_dialog.getSaveFileName(self, "Save Dockerfile", "", "Dockerfile (*.Dockerfile);;All Files (*)")

        if file_path:
            self.dockerfile_input.setText(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockerConfigApp()
    window.show()
    sys.exit(app.exec_())