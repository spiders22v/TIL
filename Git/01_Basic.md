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
