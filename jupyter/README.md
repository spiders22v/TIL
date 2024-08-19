## 1. jupyter notebook 설치

```bash
$ pip install jupyter
```

## 2. jupyter notebook 실행
```bash
$ jupyter notebook
```

## 3. jupyter notebook 서버 원격접속 설정
### 3.1 방화벽 해제
```bash
# ubuntu
$ sudo ufw allow 8888
```

### 3.2 config 파일 생성
```bash
$ jupyter notebook --generate-config
```

### 3.3 서버 비밀번호 생성

```bash
#파이썬 프롬프트 환경 실행 
$ ipython 

#비밀번호 생성 
In [1]: from jupyter_server.auth import passwd

In [2]: passwd()

Enter password: 새로운 비밀번호 입력
Verify password: 비밀번호 한번 더 입력

Out[2]: 'OOO' OOO에 해당하는  해시값 복사(config 파일에서 서버 설정에 사용)
# 종료는 ctrl+z
```

### 3.4 jupyter_notebook_config 파일 설정
에디터로 파일 열고
```bash
nano /home/spiders22v/.jupyter/jupyter_notebook_config.py
```
아래와 같이 수정

```python
#외부접속 허용
c.ServerApp.allow_origin = '*'
#작업경로 설정
c.ServerApp.notebook_dir = '작업 경로 설정' #ex: '/home/username/workspace/'
#아이피 설정
c.ServerApp.ip = '사용할 주피터 서버 ip 설정'
#포트 설정
c.ServerApp.port = 8888
#비밀번호 암호키 설정
c.ServerApp.password = u'위에서 복사한 해시값 입력'
#시작시 브라우저 실행여부
c.ServerApp.open_browser = False
```

### 3.5 jupyter notebook 실행

```bash
jupyter notebook --config /home/spiders22v/.jupyter/jupyter_notebook_config.py
```

### 외부에서 jupyter notebook 접속해서 테스트 하기
```url
주피터 서버 ip:8888
```