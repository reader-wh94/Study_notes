## Context Switching

* 현대의 멀티스레드 운영체제에서 실행 단위는 더 이상 프로세스가 아니라 스레드이다. 프로세스는 여러 개의 스레드들이 실행될 때 자원을 공유하는 컨테이너로 그 역할이 바뀌었다. 그렇기 때문에 여기서 말하는 Context Switching은 Thread 기반으로 이루어졌음을 미리 알린다.



> Context Switching

- CPU는 한번에 하나의 프로세스만 처리할 수 있다.

- 여러 프로세스를 처리해야 하는 상황에서 현재 실행중인 Task(프로세스, 스레드)의 상태를 PCB에 저장하고 다음에 진행할 Task의 상태값을 읽어 적용하는 과정을 말한다. (**다른 프로세스에게 CPU를 할당해 작업을 수행하는 과정을 말한다.**)

  <br>

> 스레드 컨텍스트와 컨텍스트 스위칭

![context_switching1](https://user-images.githubusercontent.com/68210266/154840881-2004ea5f-1fc3-45d8-9820-3d5d5c62572c.PNG)

<br>

> Context Switching 과정 (스레드1 -> 스레드2 로 변경)

1. 사용자 모드에서 커널 모드로 변경
2. 사용자 스택의 주소를 커널 스택에 저장
3. 시스템 호출 서비스 실행
4. 스레드 스케줄링 *(새로 실행시킬 스레드를 선택하기 위해 스케줄링 함수를 호출)*
5. 컨텍스트 스위칭
6. 스레드2 남은 작업 실행
7. 커널 스택에 저장된 SP레지스터 값을 CPU에 복귀
8. 스레드2의 사용자 모드로 복귀

<br>

> Over Head

* 컨텍스트 스위칭 부담
  * CPU가 사용되는 작업
  * 상당량의 CPU 시간 소모
  * 컨텍스트 스위칭의 시간이 길거나 잦은 경우 컴퓨터 처리율이 저하
* 컨텍스트 스위칭 오버헤드
  * 동일한 프로세스의 스위치로 스위칭하는 경우 *(걸리는 시간)*
    * 컨텍스트 저장 및 복귀
    * TCB 리스트 조작
    * 캐시 오버헤드
  * 다른 프로세스의 스레드로 스위칭되는 경우
    * 메모리 관련 오버헤드
    * 추가적인 캐시 오버헤드

<br>

> 비용

Context Switching의 비용은 프로세스가 스레드보다 더 많이 든다.

이유: 스레드는 Stack 영역을 제외한 모든 메모리를 공유하기 때문에 Context Switching 발생 시 stack 영역만 변경을 진행하면 되기 때문이다.

<br>

> 추가

* 프로세스 컨텍스트는 프로세스가 Running -> Ready / Blocked 상태로 갈 때 저장(or switching)되고, 프로세스가 Ready 상태에서 Running 상태로 바뀔 때 CPU에 복귀된다.

출처: [Ready-For-Tech-Interview](https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Operating%20System/Context%20Switching.md)