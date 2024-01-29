# 베이스 이미지 정의
FROM ubuntu:22.04

# 라벨 추가 (선택 사항)
LABEL maintainer="spiders22v <spiders22v@gmail.com>"

# 환경 변수 설정 (선택 사항)
ENV DEBIAN_FRONTEND=noninteractive

# 운영체제 업데이트 및 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 파이토치 설치
RUN pip3 install torch torchvision torchaudio

# 작업 디렉터리 설정 (선택 사항)
WORKDIR /app

# 현재 폴더의 ggd.py 파일을 컨테이너의 작업 디렉터리로 복사
COPY ggd.py /app/

# 컨테이너 실행 시 실행될 명령어 (선택 사항)
CMD ["python3", "ggd.py"]