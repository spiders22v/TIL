import random

def generate_lotto_numbers():
    # 1부터 45까지 숫자 중에서 6개를 중복 없이 뽑아서 리스트로 반환
    numbers = random.sample(range(1, 46), 6)
    # 뽑은 숫자들을 오름차순으로 정렬
    numbers.sort()
    return numbers

print(generate_lotto_numbers())
