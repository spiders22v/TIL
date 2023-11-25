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
