# 01 도커 소개

## 도커란?
* Go언어로 작성된 리눅스 **컨테이너** 기반으로 하는 오픈소스 가상화 플랫폼   
* 특정한 서비스를 패키징하고 배포하는데 유용한 오픈소스 프로그램

## 도커는 왜 사용하나?
**Docker을 사용하면 환경에 구애받지 않고 애플리케이션을 신속하게 배포, 확장할 수 있음**

### 기존방식(가상머신)의 단점
* OS를 가상 머신 마다 중복으로 설치하기 때문에 이밎 크키가 커짐
* 이미지가 커서 네트워크로 배포하는 것이 어려움
* 배포 및 버전 관리가 어려움
	* OS를 포함하고 있어 용량이 크기 때문에 네트워크를 통해 배포하기가 어려움
	* 이미지의 버전관리 즉 변경사항 추적이 거의 불가능
* 가상 머신은 OS안에 OS를 포함하여 가상화하여 매우 느리고 비효율적임

### 도커의 장점
* 기존 가상 머신에 비해 성능 오버헤드가 적음
* 빠르고 쉬운 애플리케이션 배포 --> 도커 이미지로 만들어서 운영서버에 전달하면됨
* 이미지 버젼 관리 쉬움
* 각 컨테이너 사이에 독립적인 동작 환경 제공 
* 마이크로 서비스 구조로 변화 용이

## 도커 이미지와 컨테이너

### 도커 이미지(Docker Image)란?
* 컨테이너를 실행할 수 있는 실행파일, 설정 값들을 가지고 있는 것으로, 더 이상 의존성 파일을 컴파일하거나 이것저것 설치할 필요가 없는 상태의 파일을 의미
* 도커 이미지를 컨테이너에 담고 실행시키면 해당 프로세스가 동작

### 도커 컨테이너(Docker Container)란?
* 도커 이미지의 실행 가능한 인스턴스
* 격리된 실행 소프트웨어 또는 동일한 애플리케이션의 빌딩 블록으로 볼 수 있음

### 도커 이미지와 컨테이너의 차이
* 도커 이미지는 설계서, 컨테이너는 설계서로 만들어진 제품
* 이미지가 중간에 바뀌어도 기존 컨테이너는 영향을 받지 않음 
<!-- ![](../assets/docker_01.png) -->
<img src="../assets/docker_01.png" width="600"/>

### 도커 이미지의 생성 방식
* 도커 이미지는 여러 개의 읽기 전용 레이어로 구성되고, 파일이 추가되면 기존 이미지에 새로운 레이어를 추가하여 구성을 올려주는 방식으로 생성
* 따라서 도커는 여러 개의 레이어를 묶어 하나의 파일시스템으로 사용할 수 있게 해줌


# 02 도커 설치

## 윈도우10/11에서 도커 설치
**Home에디션의 경우 WSL2 설치 필수, Pro 및 Enterprise 버전은 WSL2 및 Hyper-V기반 도커 엔진 사용가능**

1. 아래 링크에서  Download for Windows를 클릭해 Docker Desktop Installer를 다운로드

    [Docker Desktop for Mac and Windows | Docker](https://www.docker.com/products/docker-desktop/)

2. 다운로드 받은 Docker Desktop Installer.exe를 실행하면 사용자 계정 컨트롤이 나타나며, 설치 진행을 위해 ’예’를 클릭해 안내에 따라 설치를 진행

3. 설치 중간에 Configuration이 나타나면, 둘 다 체크하고 설치를 진행(첫 번째 옵션은 WSL 관련, 2번째 옵션은 바탕화면에 아이콘 추가할지 여부)

4. Docker Desktop 설치가 진행됩니다. 몇 분 정도 시간이 걸리니 완료될 때까지 기다림

5. 설치가 끝나면 Installation succeeded 메시지가 나타나며, 시스템 상태에 따라 재시작이나 로그아웃 할 수 있음

6. 설치된 Docker Desktop 실행
    * 시스템에 WSL2가 활성화되어있다면 Docker는 기본적으로 WSL2를 백엔드로 Docker Engine을 실행
    * 성공적으로 Docker가 실행되면 Tutorial이 나타남
  
7. WSL 통합 설정을 진행을 위해 도커 데스크톱에서 설정(Settings)으로 들어감    
    * General 설정에서 'Use the WSL 2 based engine'에 체크가 되어있는지 확인
      * 일반적으로 미리 체크가 되어있음
      * 되어있지 않다면 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭
    * Resource > WSL Integration 메뉴로 이동하여 'Enable integration with my default WSL distro' 체크되어 있는지 확인
      * 체크가 되어있지 않다면 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭하여 도커 엔진 재실행


## 우분투(리눅스)에서 도커 설치
1. 도커 APT 저장소 셋업
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. 도커 최신 패키지 설치

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. 실행 확인
```bash
sudo docker run hello-world
```

## 우분투(리눅스)에서 도커 데스크탑 설치
1. 다운로드: 최신 [DEB package](https://desktop.docker.com/linux/main/amd64/135262/docker-desktop-4.27.0-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64&_gl=1*eloknq*_ga*OTMxNTA5NjcuMTcwNjUxNTc2Ng..*_ga_XJWPQMJYHQ*MTcwNjUxNTc2Ni4xLjEuMTcwNjUxNjU5Ni4zNC4wLjA.)

2. 설치
```bash
sudo apt-get update
sudo apt-get install ./docker-desktop-<version>-<arch>.deb # 다운받은 파일
```

3. 도커 데스크탑 실행
```bash
systemctl --user start docker-desktop
```  


## 도커 설치 확인
**윈도우10/11은 Windows Terminal을 열어서 정상 동작하는지 간단하게 테스트**

1. PowerShell 탭을 하나 열고 wsl 명령어로 Docker 전용 머신이 실행중인 것을 확인
```bash
$  wsl -l -v
  NAME                   STATE           VERSION
* docker-desktop         Running         2
  docker-desktop-data    Running         2
```
2. docker version 명령으로 Docker 서버와 클라이언트 정보를 확인
```bash
$ docker version
Client:
 Cloud integration: v1.0.35+desktop.5
 Version:           24.0.6
 API version:       1.43
 ...

Server: Docker Desktop 4.25.1 (128006)
 Engine:
  Version:          24.0.6
  API version:      1.43 (minimum version 1.12)
 ...
```
3. docker ps로 실행중인 컨테이너를 확인
    * 아직 아무것도 실행중이지 않은 것을 확인할 수 있음

```bash
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**우분투에서는 콘솔창에서 정상 동작하는지 간단하게 테스트**
1. 도커 실행상태 확인

```bash
sudo systemctl status docker
```
2. 도커 실행

```bash
sudo docker run hello-world
```


## 도커 동작 확인
**nginx 이미지로 간단한 서버 테스트**
1. 웹 브라우저를 열어 127.0.0.1:9876에 접속
   * 현재 9876포트에 동작하는 서버가 없으므로 '사이트에 연결할 수 없음' 상태임
2. docker run 명령어로 nginx 이미지 기반 컨테이너를 실행하면, 이미지를 자동으로 다운받고 실행해줌
```
$ docker run -p 9876:80 -d nginx:latest
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
578acb154839: Pull complete
e398db710407: Pull complete
85c41ebe6d66: Pull complete
7170a263b582: Pull complete
8f28d06e2e2e: Pull complete
6f837de2f887: Pull complete
c1dfc7e1671e: Pull complete
Digest: sha256:ad90e201fc869b27d2f3d2ff8b7c3f575021986d0998806766012d28096cd14f
Status: Downloaded newer image for nginx:latest
83333752766cda82d28864b919772835bdb314fde80e1604ee347dd86b9d0bd7
```

3. docker ps로 실행중인 컨테이너 확인
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND                   CREATED              STATUS              PORTS                  NAMES
83333752766c   nginx:latest   "/docker-entrypoint.…"    About a minute ago   Up About a minute   0.0.0.0:9876->80/tcp   priceless_sinoussi
```

4. 다시 웹 브라우저에서 127.0.0.1:9876에 접속해보면, 이제 ‘Welcome to nginx!’ 메시지 확인
<img src="../assets/docker_02.png" width="450"/>


5. 사용하지 않는 컨테이너는 docker rm 명령어로 삭제
   * 83333752766c는 docker ps에서 확인할 수 있는 컨테이너 ID
```
$ docker rm -f 83333752766c
83333752766c
```


# 03 도커의 라이프싸이클
* pull 을 통해 이미지를 다운로드 받고 push 를 통해 Registry에 이미지 저장 가능(push 할 때 권한 필요)
* pull된 이미지를 실행하려면 create 를 통해 container를 생성해야하며, start 를 통해 container를 메모리에서 실행 가능
* run 명령어를 통해 pull , create , start 가 한 번에 수행되어 애플리케이션이 실행됨
* run과 start 명령어의 차이점은 run의 경우 이미지를 바탕으로 새로운 컨테이너를 띄우는 것이고, start는 중지된 컨테이너를 다시 시작
* 이미 pull 되어 있는 이미지의 경우 run 명령어를 사용하며 create 와 start 가 다시 실행됨
* run 을 수행할 때마다 container가 생성되므로, create 가 필요할 때만 사용하기⇒ create 와 start 를 따로 사용하는 습관을 가지는 게 BEST!!!
* stop 을 통해 container 중지 가능하며, 삭제를 원하는 경우 rm 을 사용하면됨
* 이미지 삭제를 원하는 경우 rmi 를 사용하면 됨
* 쓰고 있던 container에 대한 파일들을 이미지로 만들고 싶은 경우 commit 사용

<img src="../assets/docker_03.png" width="700"/>



# 04 많이 사용하는 커맨드

## 도커 이미지 검색 (docker search)
[도커 허브](https://hub.docker.com/)에서 이미지 검색
```bash
$ docker search [OPTIONS] TERM       # 기본 형식
$ docker search redis                # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/search/


## 도커 이미지 다운로드 (docker pull)
```bash
$ docker pull [OPTIONS] NAME[:TAG|@DIGEST]  # 기본 형식
$ docker pull redis:latest                  # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/pull/

## 컨테이너 목록 확인 (docker ps)
```bash
$ docker ps [OPTIONS]      # 기본 형식
$ docker ps                # 실행중인 모든 컨테이너 출력
$ docker ps -a             # 존재하는 모든 컨테이너 출력
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/ps/

## 이미지 목록 확인 (docker images)
도커 엔진에 존재하는 이미지 목록 확인 
```bash
$ docker images [OPTIONS] [REPOSITORY[:TAG]]
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/images/

## 컨테이너 이름 변경 (docker rename)
```bash
$ docker rename CONTAINER NEW_NAME              # 기본 형식
$ docker rename my_container my_new_container   # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/rename/

##  이미지 삭제(docker rmi)
하나 이상의 이미지를 삭제
```bash
$ docker rmi [OPTIONS] IMAGE [IMAGE...]            # 기본 형식
$ docker rmi test1:latest                          # 예시
$ docker rmi -f fd484f19954f                       # 이미지 id로 삭제
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/rmi/




# 05도커 컨테이너 생성/실행/중지

##  컨테이너 생성 (docker create)
새로운 컨테이너 생성 (실행은 안됨)
```bash
$ docker create [OPTIONS] IMAGE [COMMAND] [ARG...]   # 기본 형식
$ docker create -i -t --name mycontainer centos      # centos이미지를 이용해 mycontainer 컨테이너 생성
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/create/
- `-i` 는 상호 입출력
- `-t` 는 tty를 활성화해서 bash 셸을 사용
- create를 한 뒤 `docker ps -a` 명령어를 사용하면 생성 컨테이너의 STATUS는 `Created` 상태

##  컨테이너 시작 (docker start)
생성되거나 중지된 컨테이너 실행
```bash
$ docker start [OPTIONS] CONTAINER [CONTAINER...]     # 기본 형식
$ docker start -i mycontainer                         # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/start/
- start를 한 뒤 `docker ps -a` 명령어를 사용하면 STATUS는 `Up` 상태

##  컨테이너 접속 (docker attach)
컨테이너가 `Up` 상태일 경우 attach 명령어를 사용해서 접속이 가능
```bash
$ docker attach [OPTIONS] CONTAINER                   # 기본 형식
$ docker attach mycontainer                           # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/attach/


##  도커 이미지로 컨테이너 생성 및 실행 (docker run)

```bash
$ docker run [OPTIONS] IMAGE [COMMAND] [ARG...]       # 기본 형식
$ docker run -it --rm rockylinux:9 bash               # 예시: rockylinux:9 이미지를 사용해서, 이어지는 bash 명령어를 실행(exit로 탈출)
$ docker run -i -t  --name myredis -d redis           # 예시: redis 이미지를 사용해서 myredis로 컨테이너 이름을 지정하고, 실행
```

* ```-d``` 옵션
  * 데몬 모드로 컨테이너를 백그라운드에서 실행
  * 아래 코드에서 ```-d``` 옵션없이 실행하면, 해당 터미널에서 ```Ctrl + C``` 눌러서 빠져나오는 순간 해당 컨테이너는 종료될 것
```bash
$ docker run -d python:3.8-alpine python -m http.server
```

* ```-it``` 옵션
  * ```-i``` 옵션과 ```-t``` 옵션은 주로 함께 사용되며, 컨테이너를 종료하지 않은체로, 터미널의 입력을 계속해서 컨테이너로 전달하기 위해 사용
  * 아래 예에서는 파이썬 환경 실행
```bash
$ docker run -it python:3.8-alpine
```

* ```-name``` 옵션
  * ```-name``` 옵션을 사용해 컨테이너에 이름을 부여해주면 해당 이름으로 컨테이너를 식별할 수 있음
  * 아래 예에서는 my-server라는 이름으로 컨테이너를 실행한 후에, docker kill 커맨드로 해당 컨테이너를 종료하거나, docker rm 커맨드로 해당 컨테이너를 삭제할 때 컨테이너 이름을 컨테이너 ID 대신에 사용하고 있음
```bash
$ docker run -d --name my-server python:3.8-alpine python -m http.server
7899108d467cc423e20a3d6cb250070baae01fa541b037707afbbe8d1e9e3000
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
7899108d467c        python:3.8-alpine   "python -m http.serv…"   2 seconds ago       Up 3 second                             my-server
$ docker kill my-server
my-server
$ docker rm my-server
my-server
```

* ```-e``` 옵션
  * Docker 컨테이너의 환경변수를 설정
  * ```-e``` 옵션을 사용하면 Dockerfile의 ENV 설정도 덮어써짐
  * 아래 커맨드는 FOO 환경 변수를 bar로 세팅을 하고, 환경 변수를 출력

```
$ docker run -e FOO=bar python:3.8-alpine env
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=92ebed448fb3
FOO=bar
LANG=C.UTF-8
GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
PYTHON_VERSION=3.8.2
PYTHON_PIP_VERSION=20.0.2
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d59197a3c169cef378a22428a3fa99d33e080a5d/get-pip.py
PYTHON_GET_PIP_SHA256=421ac1d44c0cf9730a088e337867d974b91bdce4ea2636099275071878cc189e
HOME=/root
```

* ```-p``` 옵션
  * 호스트(host) 컴퓨터에서 컨테이너에서 리스닝하고 있는 포트로 접속할 수 있도록 설정
  * ```-e``` 옵션을 사용하면 Dockerfile의 ENV 설정도 덮어써짐
  * 아래 커맨드는 컨테이너 내부에서 8000 포트로 리스닝하고 있는 HTTP 서버를 호스트 컴퓨터에서 80 포트로 접속할 수 있도록 해줌

```
$ docker run -d -p 80:8000 python:3.8-alpine python -m http.server
```

* ```-v``` 옵션
  * 호스트와 컨테이너 간의 볼륨(volumn) 설정
  * 호스트(host) 컴퓨터의 파일 시스템의 특정 경로를 컨테이너의 파일 시스템의 특정 경로로 마운트(mount)를 해줌
  * 아래 커맨드는 호스트 컴퓨터의 현재 디렉토리를 컨테이너의 /etc 경로로 마운트한 후, 그 안에 있는 test.txt 파일의 내용을 출력

```
$ echo Hi > test.txt
$ docker run -v `pwd`:/etc python:3.8-alpine cat /etc/test.txt
Hi
```

* ```-w``` 옵션
  * Dockerfile의 WORKDIR 설정을 덮어쓰기 위해서 사용
  * 아래 커맨드는 컨테이너의 작업 디렉터리를 /etc로 변경함

```
$ docker run -w /etc python:3.8-alpine pwd
/etc
```

* ```-rm``` 옵션
  * 컨테이너를 일회성으로 실행할 때 사용
  * 컨테이너가 종료될 때 컨테이너와 관련된 리소스(파일 시스템, 볼륨)까지 깨끗이 제거
```bash
$ docker run --rm -it wernight/funbox nyancat
```


##  컨테이너 실행 중지(docker stop)
실행중인 하나 이상의 컨테이너를 중지
```bash
$ docker stop [OPTIONS] CONTAINER [CONTAINER...]     # 기본 형식
$ docker stop focused_payne                          # 예시: 컨테이너 이름
$ docker stop 955af8c16fdb                           # 예시: 컨테이너 ID
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/stop/


##  컨테이너 삭제(docker rm)
하나 이상의 컨테이너를 삭제
```bash
$ docker rm [OPTIONS] CONTAINER [CONTAINER...]     # 기본 형식
$ docker rm /redis                                 # 예시
$ docker rm --force redis                          # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/rm/

##  이미지 삭제(docker rmi)
하나 이상의 이미지를 삭제
```bash
$ docker rmi [OPTIONS] IMAGE [IMAGE...]            # 기본 형식
$ docker rmi test1:latest                          # 예시
$ docker rmi -f fd484f19954f                       # 이미지 id로 삭제
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/rmi/




# 06 도커 이미지 빌드

## docker commit 명령어 사용
- 간편하나 실수할 가능성이 높음
- 정말 간단한 이미지 빌드 빌드에 사용

## dockerfile 사용
- 이미지 빌드 과정을 도커파일에 저장하고 도커 빌드 명령어로 실행
- 실수가 적고 관리가 용이해 주로 사용


### Dockerfile 구성
  - FROM: 생성할 이미지의 베이스 이미지를 지정해줍니다. 여기서는 node:16-alpine이 베이스 이미지 입니다.
  - WORKDIR : 명령어를 실행할 디렉토리입니다. 배시 셸의 cd 명령어와 같은 기능을 합니다.
  - COPY : Docker 외부의 파일을 복사하여 내부에 추가합니다. COPY . . 은 현재 디렉토리에 있는 것을 전부 복사하여 workdir로 추가하는 것을 의미합니다.
  - RUN : 이미지 빌드시 실행되는 명령어입니다.
  - EXPOSE : 이미지에서 노출할 포트를 설정합니다.
  - CMD : 컨테이너 생성 시 실행되는 명령어로, Dockerfile에서 한번만 사용할 수 있습니다.

### Dockerfile 동작 방식
  - 첫 줄부터 차례로 실행
  - 한 라인이 실행 될 때 마다 이미지에 레이어 추가
  - 실행 중에 에러 발생하면 에러가 발생한 곳부터 실행
  - 첫 줄은 항상 from으로 시작
  - #으로 시작하는 것은 주석으로 인식


### Dockerfile을 이용한 이미지 빌드 예제
- 'docker_build' 폴더를 만들고, `app.py`, `requirements.txt`, `Dockerfile` 등 3개의 파일을 생성
```bash
$ mkdir docker_build
$ cd docker_build
$ touch app.py. requirements.txt, Dockerfile
```

- `app.py`에 아래 스크립트 작성 (`$ nano app.py`)
```bash
print("Hello docker")

import numpy
print(numpy.__version__)
```

- `requirements.txt`에 아래 스크립트 작성 (`$ nano requirements.txt`)
```bash
numpy==1.26.0
```

- `Dockerfile`에 아래 스크립트 작성  (`$ nano Dockerfile`)
```bash
# 기본 이미지로 우분투를 사용
FROM ubuntu:latest

# 이미지를 만든 사람의 이름과 이메일 작성
MAINTAINER spiders22v <spiders22v@gmail.com>

# 작업 디렉터리를 /app으로 설정
WORKDIR /app

# 현재 디렉터리의 모든 파일을 도커 이미지의 /app 폴더로 복사
COPY . /app

# 필요한 패키지들을 설치
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip

# 앱에 필요한 추가 패키지를 설치
RUN pip3 install -r requirements.txt

# 기본 포트(22) 노출 (예제에서는 미사용)
EXPOSE 22

# 컨테이너가 시작될 때 실행될 명령을 지정
CMD ["python3", "app.py"]
```

- `my-ubuntu-app` 이름의 이미지 빌드
  - 반드시 끝에 `.` 작성 !!! 
```bash
$ docker build -t my-ubuntu-app .
```

- 빌드된 이미지 테스트
```bash
$ docker run -it my-ubuntu-app
Hello docker    # app.py 실행결과 출력
1.26.0
```

### 기타 커맨드

- 이미지 이력 확인
```bash
$ docker history my-ubuntu-app
```

# 07 도커 이미지나 컨테이너를 파일로 관리

## 도커 이미지를 파일로 저장 (docker save)
하나 이상의 도커 이미지를 파일(tar archive)로 저장
```bash
$ docker save [OPTIONS] IMAGE [IMAGE...]           # 기본 형식
$ docker save my_image:my_tag > my_image.tar.gz    # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/save/

## 도커 이미지 파일을 불러오기 (docker load)
tar archive 나 STDIN으로부터 이미지 로드
```bash
$ docker load [OPTIONS]                            # 기본 형식
$ docker load < my_image.tar.gz                    # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/load/


## 도커 컨테이너를 파일로 저장 (docker export)
컨테이너의 파일시스템을 tar archive로 추출
```bash
$ docker export [OPTIONS] CONTAINER                   # 기본 형식
$ docker export my-container > my-container.tar.gz    # 예시
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/export/

## 도커 컨테이너를 파일을 불러오기 (docker import)
Import the contents from a tarball to create a filesystem image
```bash
$ docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]        # 기본 형식
$ cat my-container.tar.gz | docker import - my-container:m     # 로컬 파일 임포트
```
- 관련 문서: https://docs.docker.com/engine/reference/commandline/import/
- 임포트하면 컨테이너가 아닌 이미지로 불러옴 (`$docker images`로 확인)