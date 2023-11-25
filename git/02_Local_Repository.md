# 깃 저장소 (Git Repository)
* Git이 버전 관리를 하고 있는 폴더 의미
* Git에는 로컬 저장소(Local Repository)와 원격 저장소(Remote Repository)가 있음 

## 로컬 저장소 (Local Repository)
* 로컬 저장소는 사용자의 컴퓨터(로컬)에 저장된 Git 저장소
* 로컬에 있기 때문에 오프라인 상태에서도 버전 관리가 가능
* 로컬 저장소를 만드는 방법은 두 가지가 있음
  - 아직 버전 관리를 하지 않는 로컬 디렉토리를 새로운 Git 저장소로 만듦 $\Rightarrow$ ```git init```
  - 원격 저장소를 복제  $\Rightarrow$ ```git clone```

### 로컬 저장소 새로 만들기 : git init

```bash
$ git init
Initialized empty Git repository in D:/test/.git/
(main) $
```

*  디렉토리 밑에 `.git` 숨김 폴더가 생성
    - Git은 이 폴더 안에 변경 이력 등 버전 관리를 위한 파일들을 모두 저장
    - 이 디렉토리를 지우면 Git은 더이상 버전 관리를 할 수가 없음
    - 로컬 저장소를 더이상 로컬 저장소로 사용하고 싶지 않다면(버전 관리를 하고 싶지 않다면), 그냥 단순히 .git 디렉토리를 삭제하면 됨
* `(main)` 브랜치 표기

## 사용자 설정

```bash
# 유저 설정 (이름, 이메일)
git config --global user.name "username"
git config --global user.email "username@gmail.com"

# 확인
git config --global user.name
git config --global user.email

# 기본 브랜치명 변경
git config --global init.defaultBranch main
git config --global init.defaultBranch

```

