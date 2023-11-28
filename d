[1mdiff --git a/git/02_Local_Repository.md b/git/02_Local_Repository.md[m
[1mindex ce2951f..1348c76 100644[m
[1m--- a/git/02_Local_Repository.md[m
[1m+++ b/git/02_Local_Repository.md[m
[36m@@ -9,6 +9,23 @@[m
   - 아직 버전 관리를 하지 않는 로컬 디렉토리를 새로운 Git 저장소로 만듦 $\Rightarrow$ ```git init```[m
   - 원격 저장소를 복제  $\Rightarrow$ ```git clone```[m
 [m
[32m+[m
[32m+[m[32m### Git의 로컬저장소 구성[m
[32m+[m[32m- Working Directory : 사용자 작업 프로젝트의 디렉토리[m
[32m+[m[32m- Staging Area (Index) : `$ git add` 명령어로 추가한 파일들이 모여있는 공간[m
[32m+[m[32m- Repository : `$ git commit` 명령어를 실행하면 Staging Area에 있는 파일들이 하나의 버전으로 저장되는 공간[m
[32m+[m
[32m+[m[32m<img src="../assets/git_02-1.png" width="500"/>[m
[32m+[m
[32m+[m[32m### Git의 파일 상태 라이프사이클[m
[32m+[m[32m- Untracked: Working Directory에 있는 파일로써 Git으로 버전관리를 하지 않는 상태[m
[32m+[m[32m- Unmodified: 신규로 파일이 추가되었을 때, new file 상태와 같다. ( $ git add 상태 )[m
[32m+[m[32m- Modified: 파일이 추가된 이후 해당 파일이 수정되었을 때의 상태[m
[32m+[m[32m- Staged: Staging Area에 반영된 상태[m
[32m+[m
[32m+[m[32m<img src="../assets/git_02-2.png" width="500"/>[m
[32m+[m
[32m+[m
 ### 로컬 저장소 새로 만들기 : git init[m
 특정 디렉토리를 로컬 저장소로 만들고 싶다면 해당 디렉토리로 이동한 후 다음 명령어를 입력[m
 [m
[36m@@ -37,23 +54,36 @@[m [mgit clone <url> <dir_name>[m
   - VSCode의 Git 로컬 저장소가 원격 저장소로부터 복제되어 ~/happy/ 디렉토리 밑에 생성됨[m
 [m
 [m
[31m-### 로컬 저장소 추가 및 복제하기 : git add & git commit[m
[31m-- Git의 로컬저장소 구성[m
[31m-  - Working Directory : 사용자 작업 프로젝트의 디렉토리[m
[31m-  - Staging Area : `$ git add` 명령어로 추가한 파일들이 모여있는 공간[m
[31m-  - Repository : `$ git commit` 명령어를 실행하면 Staging Area에 있는 파일들이 하나의 버전으로 저장되는 공간[m
[31m-[m
[31m-<img src="../assets/git_02-1.png" width="400"/>[m
[32m+[m[32m### 로컬 저장소 Staging area 올리기: git add[m
[32m+[m[32m특정 파일을 Staging Area에 올리기 (untracked $\rightarrow$ tracked 상태로 변경)[m
 [m
[31m-- Git의 파일 상태 라이프사이클[m
[31m-  - Untracked: Working Directory에 있는 파일로써 Git으로 버전관리를 하지 않는 상태[m
[31m-  - Unmodified: 신규로 파일이 추가되었을 때, new file 상태와 같다. ( $ git add 상태 )[m
[31m-  - Modified: 파일이 추가된 이후 해당 파일이 수정되었을 때의 상태[m
[31m-  - Staged: Staging Area에 반영된 상태[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git add <file_name>[m[41m [m
[32m+[m[32m```[m
 [m
[31m-<img src="../assets/git_02-2.png" width="500"/>[m
[32m+[m[32m현재 디렉토리 및 하위에 있는 폴더/파일의 모든 변경 내용을 Staging Area에 올리기 (`.gitignore`에 있는 파일은 제외)[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git add .[m
[32m+[m[32m```[m
[32m+[m[32m작업 디렉토리 내의 모든 변경 내용을 모두 Staging Area에 올리기 (상위, 하위 모두 포함)[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git add -A[m
[32m+[m[32m```[m
[32m+[m[32m  - `git add .`명령어를 최상위 폴더에서 하게된다면 `git add -A`명령어와 동일[m
 [m
[32m+[m[32m현재 디렉토리 및 하위에 있는 폴더/파일의 모든 변경 내용을 Staging Area에 올리기 (`.gitignore`에 있는 파일도 적용)[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git add *[m[41m [m
[32m+[m[32m```[m
 [m
[32m+[m[32mUnstage(Staging Area $\rightarrow$ Working Directory)로 상태 변경[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git rm --cached[m
[32m+[m[32m```[m
[32m+[m[32mindex와 HEAD 사이의 변화를 보여줌[m
[32m+[m[32m```bash[m
[32m+[m[32m$ git diff --cached[m
[32m+[m[32m```[m
 [m
     - `git rm --cached` 명령어: unstage(Staging Area-> Working Directory)로 상태 변경[m
     - `git diff --cached` 명령어: index와 HEAD 사이의 변화를 보여줌[m
\ No newline at end of file[m
