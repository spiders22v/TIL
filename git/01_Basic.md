# 깃 (Git)이란?
* 2005년 리누스 토르발스에 의해 개발된 분산 버전관리 시스템(Distributed Version Control Systems - DVCS)
* 컴퓨터 파일의 변경사항을 추적하고 여러명의 사용자들 간에 파일에 대한 작업을 조율하는데 사용

# 버전관리는 왜 필요한가?
* 코드의 무결성을 유지하는 동시에  여러명의 사용자들 간에 파일에 대한 작업을 조율하는데 사용
* 버전에 따른 수정/변경 내용 비교, 문제발생 원인 추적 가능
* 파일 손실이나 오류 발생시 쉽게 복구 가능

# 버전 관리 시스템(VCS, Version Control System)의 종류
## 로컬 버전 관리 시스템
* 간단한 데이터베이스를 이용해 파일의 이력(변경 정보)를 관리하는 시스템
  * 예) RCS(Revision Control System): 파일에서 변경되는 부분(Patch)만 기억해 용량 문제를 해결
* 로컬에서만 동작하므로 다른 개발자와 협업을 해야 하는 상황에는 부적합 $\Rightarrow$ 이에 중앙 집중식 관리시스템 등


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
