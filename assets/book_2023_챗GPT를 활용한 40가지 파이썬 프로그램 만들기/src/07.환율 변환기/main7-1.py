import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox

import requests

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # GUI 요소 생성
        self.label_amount = QLabel('변환할 금액:')
        self.edit_amount = QLineEdit()

        self.label_base_currency = QLabel('기준 통화:')
        self.combo_base_currency = QComboBox()
        self.combo_base_currency.addItems(['KRW', 'USD', 'JPY'])

        self.label_target_currency = QLabel('변환 통화:')
        self.combo_target_currency = QComboBox()
        self.combo_target_currency.addItems(['KRW', 'USD', 'JPY'])

        self.label_result = QLabel('변환 결과:')

        self.btn_convert = QPushButton('환율 변환')
        self.btn_convert.clicked.connect(self.convert_currency)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label_amount)
        layout.addWidget(self.edit_amount)
        layout.addWidget(self.label_base_currency)
        layout.addWidget(self.combo_base_currency)
        layout.addWidget(self.label_target_currency)
        layout.addWidget(self.combo_target_currency)
        layout.addWidget(self.label_result)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)

        # 윈도우 설정
        self.setWindowTitle('Currency Converter')
        self.setGeometry(300, 300, 400, 200)

    def get_exchange_rate(self, base_currency, target_currency):
        # Open Exchange Rates API Key (YOUR_API_KEY)를 발급받아 대체해주세요.
        api_key = 'YOUR_API_KEY'
        api_url = f'https://open.er-api.com/v6/latest/{base_currency}'
        params = {'apikey': api_key}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            rates = data.get('rates', {})
            exchange_rate = rates.get(target_currency)
            if exchange_rate is not None:
                return exchange_rate
            else:
                self.label_result.setText(f"환율 정보를 찾을 수 없습니다. (기준: {base_currency}, 대상: {target_currency})")
        else:
            self.label_result.setText(f"API 호출에 실패했습니다. (Status Code: {response.status_code})")

        return None

    def convert_currency(self):
        amount = float(self.edit_amount.text())
        base_currency = self.combo_base_currency.currentText()
        target_currency = self.combo_target_currency.currentText()

        exchange_rate = self.get_exchange_rate(base_currency, target_currency)

        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            self.label_result.setText(f"{amount} {base_currency}은(는) 현재 환율에 따라 {converted_amount:.2f} {target_currency}입니다.")
        else:
            self.label_result.setText("환율 변환에 실패했습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec_())
