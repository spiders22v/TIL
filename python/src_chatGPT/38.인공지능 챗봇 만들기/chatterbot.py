from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 챗봇 생성
chatbot = ChatBot("SimpleChatBot")

# 언어 트레이너 생성 및 훈련
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.korean")

# 사용자 입력에 대한 응답
while True:
    user_input = input("사용자: ")
    
    # "종료"를 입력하면 프로그램 종료
    if user_input == '종료':
        print("챗봇을 종료합니다.")
        break

    # 챗봇의 응답 출력
    response = chatbot.get_response(user_input)
    print(f"챗봇: {response}")
