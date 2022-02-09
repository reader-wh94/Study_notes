## Git-branch란?

### 1. Branch 정의

영어 단어 그대로의 branch는 나뭇가지이다.

이를 Git에 적용해보면 큰 줄기(main)에서 뻗어나오는 가지(branch)라고 생각하면 된다.



주로 git init 시 자동으로 생성해주는 main 브랜치를 뼈대로 사용하기도 한다.

branch는 독립적인 작업 공간을 생성하는 아주 중요한 개념이다. 뼈대가 되는 branch에서 추가 테스트 및 추가 버전을 구현하고 싶을 경우 최신 버전을 그대로 가져와 새로운 작업 공간에서 원하는 것을 구현할 수 있도록 해주는 것이 branch이다. 

만약 branch가 없을 경우에는 계속해서 프로젝트 폴더를 복사하여 진행해야 할 것이다. 하지만 만약 추가 기능 구현 및 테스트 후, 해당 코드를 메인 버전에 통합하고 싶을 경우에는 어떻게 진행해야 하는가? 

이럴 때를 위하여 branch는 독립적인 공간을 제공하므로 테스트, 통합 등의 기능을 사용할 수 있다.



### 2. Git Branch 종류

Gitflow Workflow에서는 항상 유지되는 메인 브랜치들(main, develop)과 일정 기간 동안만 유지되는 보조 브랜치들(feature, release, hotfix)을 포함하여 총 5가지의 브랜치를 사용한다.



### 2-1. Main Branch

제품으로 출시될 수 있는 브랜치이다.

배포(Release) 이력을 관리하기 위해 사옹한다. 즉, 배포 가능한 상태만을 관리한다.

![branch1](https://user-images.githubusercontent.com/68210266/153139119-0c17d9c3-801d-4bc4-b8dc-94c29b54de98.PNG)



### 2-2. Develop Branch (dev)

다음 출시 버전을 개발하는 브랜치다.

기능 개발을 위한 브랜치들을 병합하기 위해 사용한다. 즉, 모든 기능이 추가되고 버그가 수정되어 배포 가능한 안정적인 상태하면  develop 브랜치를 'main' 브랜치에 병합(merge) 한다.

평소에는 이 브랜치를 기반으로 개발을 진행한다.

![branch2](https://user-images.githubusercontent.com/68210266/153139371-baa409db-0b18-4ce2-9c23-a81b5b207fd6.PNG)



### 2-3. Feature Branch

기능을 개발하는 브랜치

feature 브랜치는 새로운 기능 개발 및 버그 수정이 필요할 때마다 'develop' 브랜치로부터 분기한다. feature 브랜치에서의 작업은 기본적으로 공유할 필요가 없기 때문에, 자신의 로컬 저장소에서 관리한다.

개발이 완료되면 'develop' 브랜치로 병합(merge)하여 다른 사람들과 공유한다.

1. ‘develop’ 브랜치에서 새로운 기능에 대한 feature 브랜치를 분기한다.
2. 새로운 기능에 대한 작업 수행한다.
3. 작업이 끝나면 ‘develop’ 브랜치로 병합(merge)한다.
4. 더 이상 필요하지 않은 feature 브랜치는 삭제한다.
5. 새로운 기능에 대한 ‘feature’ 브랜치를 중앙 원격 저장소에 올린다.(push)
   * feature 브랜치의 이름은 [feature/기능] 형식을 주로 사용한다. ex) feature/login





![branch3](https://user-images.githubusercontent.com/68210266/153139776-28dff4f6-78c8-43c1-a7b0-9fdf969201c6.PNG)



### 2-4. Release Branch / Hotfix Branch

Release branch는 이번 출시 버전을 준비하는 브랜치다.

Hotifx branch는 출시 버전에서 발생한 버그를 수정하는 브랜치다.

이 둘의 브랜치는 따로 사용해 본 적이 많지 않기 때문에 2번째 출처를 확인했으면 한다.



### 3. Git Branch 사용 방법



출처: [Git\] 명령어(3) - branch🐵](https://victorydntmd.tistory.com/75), [[GitHub] Git 브랜치의 종류 및 사용법 (5가지)](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html)

