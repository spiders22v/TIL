### GIT이란?
* 2005년 리누스 토르발스에 의해 개발된 분산 버전관리 시스템(Distributed Version Control Systems - DVCS)
* 컴퓨터 파일의 변경사항을 추적하고 여러명의 사용자들 간에 파일에 대한 작업을 조율하는데 사용


## 로컬 저장소 설정

```bash
$ git init
Initialized empty Git repository in D:/test/.git/
(main) $
```

* `.git` 숨김 폴더가 생성
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
