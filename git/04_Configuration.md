## Git 설정하기 : git config
Git은 다음과 같이 세 종류의 config 파일을 사용함
* `.git/config`: Git 저장소 안의 .git 디렉토리 밑에 저장되는 config 파일로, 해당 Git 저장소에만 적용
  - 서로 다른 Git 저장소 간에 서로 다른 설정을 할 수 있음
  - 가장 우선순위가 높음 $\Rightarrow$ 즉, 다른 config 파일에 동일한 설정 항목이 있을 경우 .git/config 파일의 설정이 우선함
* `~/.gitconfig` 혹은 `~/.config/git/config`: 사용자의 홈 디렉토리 밑에 저장되는 config 파일로, 해당 사용자에만 적용
  - 이를 이용하면 서로 다른 사용자 간에 서로 다른 설정을 할 수 있음
  - 두 번째로 우선순위가 높음
* `/etc/gitconfig`: 시스템 폴더인 /etc/ 폴더 밑에 저장되는 설정으로, 시스템의 모든 사용자와 모든 Git 저장소에 적용
  - 이곳에 설정값을 저장하기 위해서는 관리자 권한이 필요함
  - 가장 우선순위가 낮음

config 파일에 설정값을 저장하기 위해서는 `git config` 명령어를 사용
* `git/config` 파일에 설정값을 저장하려면 아무런 옵션을 주지 않거나 `--local` 옵션을 주면 됨
* `~/.gitconfig` 파일에 설정값을 저장하려면 `--global` 옵션을 주면 됨
* `/etc/gitconfig` 파일에 설정값을 저장하려면 `--system` 옵션을 주면 됨

## 사용자 정보 설정하기
Git에서 변경사항을 저장(commit)하기 위해서는 사용자의 정보(이름과 이메일 주소)가 필요하며, Git은 config 파일로부터 사용자의 정보를 읽어 변경사항을 저장함

사용자 정보는 다음과 같이 저장함
```bash
$ git config user.name "<user_name>"
$ git config user.email "<user_email>"
```
* `<user_name>`: 사용자 이름
* `<user_email>`: 사용자 이메일

예시: 
```bash
$ git config user.name "spiders22v"                              # .git/config에 저장
$ git config user.email "spiders22v@gmail.com"                   # .git/config에 저장

$ git config --local user.name "spiders22v"                      # .git/config에 저장
$ git config --local user.email "spiders22v@gmail.com"           # .git/config에 저장

$ git config --global user.name "spiders22v"                     # ~/.gitconfig에 저장
$ git config --global user.email "spiders22v@gmail.com"          # ~/.gitconfig에 저장

$ sudo git config --system user.name "spiders22v"                # /etc/gitconfig에 저장
$ sudo git config --system user.email "spiders22v@gmail.com"     # /etc/gitconfig에 저장
```

## 기본 텍스트 편집기 설정하기
Git에서는 커밋, 병합 등에서 텍스트 편집기를 사용하며, 다음 명령어로 원하는 편집기를 사용하게 만들 수 있음
```bash
$ git config core.editor "<editor_name>"
```
* `<editor_name>`: 에디터 이름

우분투에서는 nano가 시스템 기본 편집기이며, 다음과 같이 하면 vim을 기본 에디터로 설정할 수 있음
```bash
$ git config --global core.editor vim
```

## 설정값 읽기
다음 명령어는 모든 설정값을 읽는 명령어
```bash
$ git config --list
```
* `.git/config`, `~/.gitconfig`, `/etc/gitconfig`에 동일한 설정값이 있다면 실제 적용되는 설정값(가장 우선순위가 높은 설정값)이 출력

다음 명령어는 특정 설정값을 읽는 명령어
```bash
$ git config "<key>"
```
* `<key>`: 옵션 이름 (ex. `user.name`, `user.email`, `core.editor`, etc.)
* `.git/config`, `~/.gitconfig`, `/etc/gitconfig`에 동일한 설정값이 있다면 실제 적용되는 설정값(가장 우선순위가 높은 설정값)이 출력

`--show-origin` 옵션을 주면 여러 config 파일 중 어디서 설정값을 읽어 왔는지(실제 어떤 설정값이 적용되고 있는지)를 보여줌
```bash
$ git config --show-origin "<key>"
```




