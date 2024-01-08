import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QLabel, QPushButton


class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 단위변환 프로그램 제목
        self.setWindowTitle("Unit Converter")
        
        # 입력 필드
        self.value_input = QLineEdit(self)
        self.value_input.setGeometry(20, 20, 150, 30)
        
        # 입력 단위 선택
        self.unit_from = QComboBox(self)
        self.unit_from.addItems(["Celsius", "Fahrenheit", "Meter", "Feet"])
        self.unit_from.setGeometry(180, 20, 100, 30)
        
        # 출력 단위 선택
        self.unit_to = QComboBox(self)
        self.unit_to.addItems(["Fahrenheit", "Celsius", "Feet", "Meter"])
        self.unit_to.setGeometry(290, 20, 100, 30)
        
        # 변환 버튼
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setGeometry(400, 20, 100, 30)
        self.convert_button.clicked.connect(self.convert)
        
        # 결과 출력
        self.result_label = QLabel("", self)
        self.result_label.setGeometry(20, 80, 480, 30)
        
        # 윈도우 크기 및 위치 설정
        self.setGeometry(300, 300, 520, 150)
        self.show()
    
    def convert(self):
        # 사용자로부터 입력값과 단위를 가져옴
        value = float(self.value_input.text())
        unit_from = self.unit_from.currentText()
        unit_to = self.unit_to.currentText()
        
        # 입력받은 단위에 따라 변환 수행
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            result = value * 9/5 + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            result = (value - 32) * 5/9
        elif unit_from == "Meter" and unit_to == "Feet":
            result = value * 3.281
        elif unit_from == "Feet" and unit_to == "Meter":
            result = value / 3.281
        else:
            result = "Invalid input"
        
        # 결과를 레이블에 출력
        self.result_label.setText("{:.2f} {} = {:.2f} {}".format(value, unit_from, result, unit_to))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    sys.exit(app.exec_())
