## 교착상태 (DeadLock)

> 교착상태의 정의

* 자원을 소유한 스레드(or 프로세스)들 사이에서 각 스레드는 다른 스레드가 소유한 자원을 요청하여 모든 스레드가 무한정 대기하는 현상

* 치명적인 포옹(deadly embrace)라고도 한다

<br>

> 교착상태의 사례

* 두 스레드가 임계구역에 진입하기 위해 2개의 락 LockA, LockB를 모두 필요로 하는데, 각 스레드가 락(lock)을 요청하는 경우이다.

<img src="https://user-images.githubusercontent.com/68210266/155941001-1cdd528e-79df-45dd-9452-5d4b32987605.PNG" alt="deadlock1" style="zoom:50%;" />

* 교착상태는 단일 CPU나 다중 CPU를 가리지 않고, 락(lock)이나 자원에 대한 다중 스레드의 경쟁이 있는 한 발생할 수 있다.

<br>

> 교착상태 유발의 잠재적 요인

* 자원 : 교착상태의 발생지
* 자원과 스레드 : 한 스레드가 동시에 여러 개의 자원을 필요로 하는 경우
* 자원과 운영체제 : 운영체제는 한 번에 하나씩 자원을 할당
* 자원 비선점 : 할당된 자원은 스레드가 자발적으로 내놓기 전에 강제로 뺐지 못한다. 

<br>

> 교착상태 발생 조건

* 4가지 조건이 동시에 성립할 때 발생한다.
* 4가지 조건 중 1개라도 성립하지 않는다면 교착상태는 발생하지 않는다.

1. 상호배제(Mutual Exclusion)
   * 자원은 한 번에 한 스레드에게 할당 가능
   * 자원이 한 스레드에게할당되면 다른 스레드에게는 할당될 수 없음
2. 소유하면서 대기(Hold & Wait)
   * 스레드가 한 자원을 소유하면서(lock) 다른 자원을 요청하여 대기
3. 강제 자원 반환 불가(No Preemption)
   * 스레드에게 할당된 자원은 강제로 빼앗지 못함
4. 순환 대기(Circular Wait)
   * 한 그룹의 스레드들 사이에서, 각 스레드는 다른 스레드가 요청하는 자원을 소유하는 순환 고리 형성

<br>

> 교착상태 해결 방법

* 교착상태 예방(prevention)

  * 4가지 조건 중 하나 이상의 조건이 아예 성립되지 못하도록(금지, prevent) 시스템을 설계하고 구성하여 교착상태가 발생할 여지를 차단한다.

  1. 상호배제
     * 자원이 한 스레드에 의해 독점되는 것을 막기 위해 자원을 2개의 스레드가 동시에 사용할 수 있도록 허용한다.
     * 하지만 근본적으로 불가능하다.
  2. 소유하면서 대기
     * 스레드 실행 전에 스레드가 필요로 하는 자원을 모두 알고, 스레드 실행 시작과 함께 모든 자원을 할당해주어 실행 중에 자원을 요청하여 대기하는 일이 없도록 한다.
     * 스레드가 몇 개의 자원을 소유한 상태에서 실행 중 새로운 자원이 필요하게 되면, 현재 할당받은 모든 자원을 반환하고 필요한 모든 자원을 한꺼번에 모두 요청하는 방법이다. 
  3. 강제 자원 반환 불가
     * 더 높은 순위의 스레드가 자원을 요청하며 운영체제가 그 자원을 가진 낮은 순위의 스레드로부터 강제로 자원을 반환할 수 있게 한다.
  4. 순환 대기
     * 모든 자원에 번호를 매기고, 반드시 번호 순으로 자원을 할당받게 하는 방법

* 교착상태 회피(avoidance)

  * 자원을 할당할 때 교착상태에 빠지지 않을 것이라고 확신하는 경우에만 자원을 할당하는 방법이다.
  * 순환 대기가 발생할 것인지 판단되면 자원을 할당하지 않음으로써 교착상태의 발생을 피한다.

* 교착상태 감지 및 복구(detection and recovery)

  * 교착상태의 예방이나 회피 전략을 가동하지 않고, 운영체제가 교착상태를 감지하는 별도의 프로그램을 백그라운드로 구동시켜, 교착상태에 빠진 스레드 그룹이 있다면 이들을 교착상태로부터 해제시키는 방법이다.
  * 교착상태를 감지하는 백그라운드 작업이 늘 실행되므로 시스템에는 많은 부담이 된다.\

  1. 자원 강제 선점(preemption)
     * 교착상태에 빠진 스레드 중 하나를 선택하고 이 스레드가 소유한 자원을 강제로 빼앗아 이 자원을 기다리는 다른 스레드에게 할당하는 방법
  2. 롤백(rollback)
     * 운영체제는 교착상태가 발생할 것으로 예측되는 스레드들에 대해 그들의 상태를 주기적으로 저장해두었다가, 교착상태가 발생하면 가장 최근에 저장해둔 상태로 복구시켜 가장 최근에 실행하던 상태로 돌아가게 한다.
  3. 스레드 강제 종료(kill process)
     * 교착상태에 빠진 스레드 중 하나를 강제로 종료시키는 방법이다.

* 교착상태 무시(ignore and reboot)

  * 교착상태에 아무런 대비책 없이 발생하도록 내버려 두는 방법이다
  * 주로 ostrich 알고리즘을 사용하여 교착상태를 무시한다.

  <br>

  1. 타조(ostrich) 알고리즘
     * 교착상태에 대한 아무런 대책 없이 컴퓨터 시스템을 가동시키고, 교착상태가 발생하면 시스템을 재시작(reboot)하거나 특정 스레드를 강제 종료하는 방법으로 해결한다.

<br>

