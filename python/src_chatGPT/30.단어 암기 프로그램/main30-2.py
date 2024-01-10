import random

def load_words(filename):
    words = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word, meaning = line.strip().split(":")
            words[word] = meaning
    return words

def quiz(words):
    word_list = list(words.keys())
    random.shuffle(word_list)
    for word in word_list:
        meaning = words[word]
        answer = input(f"{word}의 뜻은 무엇일까요? ")
        if answer == meaning:
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은 {meaning}입니다.")

if __name__ == "__main__":
    filename = r"30.단어 암기 프로그램\단어.txt"
    words = load_words(filename)
    quiz(words)
