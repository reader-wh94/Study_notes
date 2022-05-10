## 개인적으로 자주 사용하는 Git 명령어

### 1. 가장 최근(마지막)의 commit 수정

> 로컬에서 commit 메세지를 작성 완료, But push는 하지 않은 상태

```bash
$ git commit --amend
```

<br>

### 2. git add 취소하기

```bash
$ git reset HEAD [file]
// [file]의 add를 취소

$ git reset HEAD
// add한 파일 전체를 취소
```

<br>

### 3. git commit 취소하기

```bash
$ git reset --soft HEAD^
// [방법 1] commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존

$ git reset --mixed HEAD^ // 기본 옵션
// [방법 2] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존

$ git reset HEAD^ // 위와 동일

$ git reset HEAD~2 // 마지막 2개의 commit을 취소

$ git reset --hard HEAD^
// [방법 3] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
```

git reset 옵션

* –soft : index 보존(add한 상태, staged 상태), 워킹 디렉터리의 파일 보존. 즉 모두 보존.
* –mixed : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 보존 (기본 옵션)
* –hard : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 삭제. 즉 모두 취소

<br>



출처

https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html

https://velog.io/@mayinjanuary/git-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%84%B8%EC%A7%80-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0-changing-commit-message

