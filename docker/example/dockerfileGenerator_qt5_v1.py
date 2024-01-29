import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QTextEdit, QComboBox

class DockerfileGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dockerfile Generator')
        self.setGeometry(100, 100, 400, 400)

        self.label_from = QLabel('FROM:')
        self.combo_from = QComboBox(self)
        self.combo_from.addItems(['ubuntu:18.04', 'ubuntu:20.04', 'ubuntu:latest'])

        self.label_add = QLabel('ADD:')
        self.edit_add = QLineEdit(self)

        self.label_copy = QLabel('COPY:')
        self.edit_copy = QLineEdit(self)

        self.label_run = QLabel('RUN:')
        self.edit_run = QLineEdit(self)

        self.label_cmd = QLabel('CMD:')
        self.edit_cmd = QLineEdit(self)

        self.label_expose = QLabel('EXPOSE:')
        self.edit_expose = QLineEdit(self)

        self.label_env = QLabel('ENV:')
        self.edit_env = QLineEdit(self)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        self.btn_generate = QPushButton('Generate Dockerfile', self)
        self.btn_generate.clicked.connect(self.generate_dockerfile)

        self.btn_build_image = QPushButton('Build Docker Image', self)
        self.btn_build_image.clicked.connect(self.build_docker_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label_from)
        layout.addWidget(self.combo_from)
        layout.addWidget(self.label_add)
        layout.addWidget(self.edit_add)
        layout.addWidget(self.label_copy)
        layout.addWidget(self.edit_copy)
        layout.addWidget(self.label_run)
        layout.addWidget(self.edit_run)
        layout.addWidget(self.label_cmd)
        layout.addWidget(self.edit_cmd)
        layout.addWidget(self.label_expose)
        layout.addWidget(self.edit_expose)
        layout.addWidget(self.label_env)
        layout.addWidget(self.edit_env)
        layout.addWidget(self.btn_generate)
        layout.addWidget(self.btn_build_image)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def generate_dockerfile(self):
        dockerfile_content = f'FROM {self.combo_from.currentText()}\n'

        if self.edit_add.text():
            dockerfile_content += f'ADD {self.edit_add.text()}\n'

        if self.edit_copy.text():
            dockerfile_content += f'COPY {self.edit_copy.text()}\n'

        if self.edit_run.text():
            dockerfile_content += f'RUN {self.edit_run.text()}\n'

        if self.edit_cmd.text():
            dockerfile_content += f'CMD {self.edit_cmd.text()}\n'

        if self.edit_expose.text():
            dockerfile_content += f'EXPOSE {self.edit_expose.text()}\n'

        if self.edit_env.text():
            dockerfile_content += f'ENV {self.edit_env.text()}\n'

        self.output_text.setPlainText(dockerfile_content.strip())

    def build_docker_image(self):
        dockerfile_content = self.output_text.toPlainText()
        
        if not dockerfile_content:
            return  # No Dockerfile content to build

        try:
            # Save Dockerfile content to a temporary file
            with open('Dockerfile', 'w') as dockerfile:
                dockerfile.write(dockerfile_content)

            # Build Docker image using subprocess
            subprocess.run(['docker', 'build', '-t', 'custom-image:latest', '.'])
        except Exception as e:
            print(f"Error building Docker image: {e}")
        finally:
            # Remove the temporary Dockerfile
            # subprocess.run(['rm', 'Dockerfile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Quit the application after image build
            QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockerfileGenerator()
    window.show()
    sys.exit(app.exec_())
