## 뮤텍스(Mutex) VS 세마포(Semaphore)

> 사전 설명

* [상호배제](https://github.com/reader-wh94/Study_notes/blob/master/Operating%20System/%EC%83%81%ED%98%B8%EB%B0%B0%EC%A0%9C%20(Mutual%20exclusion).md)
* 상호배제 장치(mutual exclusion device), 동기화 프리미티브(synchronization primitive) : 상호배제를 기반으로 여러 스레드들이 공유 자원을 액세스하는 전통적인 스레드 동기화 기법
* 대표적인 동기화 기법
  * 락(lock) 방식 : 뮤텍스(mutex), 스핀락(spinlock)
  * wait-signal 방식 : 세마포(semaphore)

<br>

> 뮤텍스(Mutex)

* 뮤텍스는 잠김/열림(locked / unlocked) 중 한 상태를 가지는 락 변수를 이용하여 오직 한 스레드만이 자원을 배타적으로 사용하도록 하는 기법이다.
* 락이 걸려있는 경우, 임계구역에 들어가려고 하는 스레드가 락이 풀릴 때까지 블록 상태로 큐에서 대기하기 때문에 blocking lock 기법이라고도 부르고, 대기 큐에서 잠자면서 기다린다고 해서 sleep-waiting lock 기법이라고도 부른다.
* 목적 : 임계구역에 대한 한 스레드의 배타적 접근

* 특징
  * 임계구역의 실행시간이 짧은 경우, 뮤텍스는 비효율성을 보인다.
* 뮤텍스 동기화의 구조

![mutex](https://user-images.githubusercontent.com/68210266/155885993-107ec8f3-4dd8-4e4c-b803-80960b5cf457.PNG)

<br>

> 세마포

* 세마포는 스레드가 동시에 사용할 수 있는 하나의 자원에 대해 스레드가 공유하도록 관리하는 동기화 프로그래밍 기법이며  프로그래밍 개념(concept)이다.
* 세마포 요소
  * 자원 : n개의 인스턴스
  * 대기 큐 : 자원을 할당받지 못한 스레드가 잠드는 곳
  * counter 변수 : 사용가능한 자원의 개수를 나타내는 정수형 전역 변수로 자원의 개수 n으로 초기화 된다.
  * P/V 연산: P 연산은 자원 요청 시, V 연산은 자원 반환 시 실행되는 연산

* 목적 : 자원에 대한 다중 스레드의 원활한 공유
* 세마포 동기화 구조

![semaphore](https://user-images.githubusercontent.com/68210266/155886013-e6f22f7f-a5e9-428a-9bbe-933b5ed92cf3.PNG)

<br>

> 세마포 - P/V 연산

* P/V 연산은 wait/signal 연산으로도 불린다.
* P 연산은 스레드의 자원 사용을 허가한다.
* P 연산은 counter 변수를 1 감소시키고 V 연산은 counter 변수를 1 증가 시킨다.
* P/V 연산은 sleep-wait 세마포와 busy-waiting 세마포로 나뉜다.
  * sleep-wait 세마포
    * P 연산 중 자원 사용을 허가받지 못한 스레드는 사용가능한 자원이 생길 때까지 대기 큐에서 잠을 자고(sleep-wait), V 연산에 의해 사용가능한 자원이 생기게 되면 깨어나서 자원 사용을 허가 받는 형태이다.
  * busy-waiting 세마포
    * P 연산에서 사용가능한 자원이 생길 때까지 무한 루프를 돌면서 체크(busy-waiting)한다. 그러다가 V 연산에 의해 가용자원이 생기면, P 연산에서 자원을 획득하는 방식이다.
    * 대기 큐가 필요 없다.