import requests

def currency_converter(amount, from_currency, to_currency):
    # API 호출 URL
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    # API 호출 및 응답 받기
    response = requests.get(url)
    data = response.json()
    
    # 환율 계산
    exchange_rate = data['rates'][to_currency]
    result = round(amount * exchange_rate, 2)
    
    # 결과 반환
    return result


print("환율 변환기")
print("============")

while True:
    try:
        # 변환하려는 금액 입력
        amount = float(input("변환하려는 금액을 입력하세요: "))
        
        # 변환하려는 화폐 입력
        from_currency = input("어떤 화폐에서 변환하시겠습니까? (예: USD, KRW): ").upper()
        to_currency = input("어떤 화폐로 변환하시겠습니까? (예: USD, KRW): ").upper()
        
        # 환율 계산
        result = currency_converter(amount, from_currency, to_currency)
        
        # 결과 출력
        print(f"{amount} {from_currency}은(는) {result} {to_currency}입니다.")
        
        # 계속 변환할지 묻기
        choice = input("계속 변환하시겠습니까? (Y/N): ").upper()
        if choice != "Y":
            break
            
    except:
        print("올바른 값을 입력해주세요.")
