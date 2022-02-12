## Git 잔디가 안심어질 때

----

Git bash에서 commit하고 push를 했는데 contribution에 잔디가 심어지지 않을 때가 있다.

나중에 또 헤멜 나를 위해 기록한다!



### 1번 방법 - Git 계정 확인

**git config user.email**을 통해 계정을 확인하자

```bash
🚩 계정 확인 방법
git config --global user.name
git config --global user.email

🗽 계정 변경 방법
git config --global user.name "USER_NAME"
git config --global user.email "USER_EMAIL"
```



### 2번 방법 - Branch 확인

merge한 브랜치가 main(master) 브랜치가 아닐 때 잔디가 심어지지 않는 경우가 있다.

(사실 최근에 이 문제로 나에게 질문한 동생이 있었다. 방법은 대충 알려줬는데 제대로 했을 지는 모르겠다..)



즉, 만약에 내가 develop 브랜치에서 작업을 했는데 master 브랜치가 default 브랜치일 경우 contribution 기록이 남지 않는다. 이럴 경우에는 default 브랜치를 develop으로 변경해도 되지만 나중에 develop 브랜치를 master 브랜치로 merge하면 일괄적으로 contribution에 적용될 것이다!



출처: [[git] github 잔디가 심어지지 않아요!](https://pongsoyun.tistory.com/122)