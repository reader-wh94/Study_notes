## Git pull request 알아보기

### 1. Fork

* PR을 날릴 타겟 프로젝트의 저장소를 자신의 저장소로 Fork 한다.



### 2. clone, remote

* fork로 생성한 본인 계정의 저장소에서 clone or download 버튼을 누르고 url을 복사한다.
* 터미널을 켠다.
* 자신이 사용하는 로컬 컴퓨터에 Fork한 저장소를 clone한다.
  * ```$ git clone http://```
* 로컬 저장소에 원격 저장소를 추가한다.
  * ```$ git remote add project(별명) http://~```
  * ```$ git remote -v```



### 3. branch 생성

* 로컬 컴퓨터에서 수정하는 내용들은 branch를 생성하여 진행한다.
  * ```$ git checkout -b develop```
    * develop이란 브랜치 생성 후 master branch에서 develop 브랜치로 이동
    * 후에 작업하는 commit 들은 develop branch에서만 일어난다.



### 4. 수정 작업 후 add, commit, push

* 코드 수정, 추가 등의 작업을 진행한다.
* 작업이 완료되면 add, commit, push 단계를 거쳐 자신의 github repository(origin)에 수정 사항을 반영한다.
* push 진행 시 branch 이름을 꼭! 적어야한다.
  * ```$ git push origin develop```



### 5. Pull Request 생성

* push 완료 후 본인 계정의 github 저장소에 들어가면 Compare & pull request 버튼이 활성화되어 있다.
* 해당 버튼을 선택하여 메세지를 작성하고 PR을 생성한다.



### 6. Merge pull Request

* PR을 받은 원본 저장소 관리자(자신이 Fork 해 온 레포지토리 관리자)는 코드 변경 내역을 확인하고 Merge 여부를 결정한다.



### 7. Merge 이후 동기화 및 branch 삭제

* 원본 저장소에 Merge가 완료되면 로컬 코드와 원본 저장소의 코드를 동기화 한다.
  * ```$ git pull project(remote 별명)```
  * ```$ git branch -d develop```



### 개인 사담

졸업 작품 진행 했을 때와 같은 순서였다! pull request를 통해서 한 명의 원본 관리자가 관리하는 형식이 아니라 우린 다들 PR을 생성하지 않고 각자 원본 저장소에 Merge를 했던 것이었다.

PR이 뭔지 말만 들어봤지 어떻게 하는 지 몰라서 아래 블로그를 참고해봤는데, 작년에 졸작하는 내내 썼던 git 명령어들 사이에 PR을 생성하는 것  하나만 빠진 것이다.



출처: https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/