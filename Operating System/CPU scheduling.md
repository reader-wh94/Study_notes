## CPU scheduling

> CPU scheduling

CPU 스케줄링이란 메모리에서 실행을 기다리는 프로세스 중, 하나를 선택하는 과정이다. 

CPU 스케줄링의 목표는 CPU의 유휴시간 줄이기, 컴퓨터 시스템 처리율 향상이다.

<br>

> CPU 스케줄링의 기준

* 높은 CPU 활용률(CPU utilization) - 컴퓨터의 전체 가동 시간에 대한 CPU의 사용 시간의 비율
* 처리율 극대화(maximize throughput) - 단위 시간 당 처리하는 프로세스의 개수를 극대화
* 공정성(fairness) - 모든 프로세스에게 CPU 사용 시간을 공평하게 배분
* 응답 시간 최소화(minimize response time) - 대화식 사용자에 대한 응답 시간을 최소화
* 대기 시간 최소화(minimize waiting time) - 프로세스가 준비 리스트에서 CPU를 할당받을 때까지 대기 시간
* 소요 시간 최소화(minimize turnaround time) - 작업을 시작시킨 사용자가 결과를 얻기까지 걸린 총 시간
* 시스템 정책 시행 우선(high policy enforcement) - 스케줄링이 컴퓨터 시스템의 정책에 맞도록 이루어져야함
* 자원 활용률 극대화(high resource efficiency)

<br>

> CPU 스케줄링과 타임 슬라이스(time slice)

대부분의 운영체제들은 하나의 프로세스나 스레드가 너무 오래 CPU를 사용하도록 허용하지 않는다. 운영체제 커널은 타이머의 도움을 받아 **주기적으로 CPU 스케줄링을 단행하는데 이 주기 시간을 타임 슬라이스(time slice)**라고 부른다.

타임 슬라이스마다 커널은 실행되고 있는 현재 프로세스나 스레드를 강제로 중단시켜(preemption) 준비 리스트에 삽입한다. 그리고 다른 프로세스나 스레드를 스케줄하고 타임 슬라이스 동안 CPU를 사용하도록 한다.

<br>

> CPU 스케줄링이 시행되는 상황

1. 프로세스나 스레드가 I/O를 요청하는 시스템 호출 시, 블록 상태(block state)가 되거나 요청한 자원을 기다리는 상태(wait state)가 될 때 커널은 CPU 스케줄링을 시행한다(CPU의 idle을 막는 목적).
2. 프로세스나 스레드에게 할당된 CPU 사용 시간(time slice)이 다 되어 타이머 인터럽트가 발생할 때, 커널은 CPU 스케줄링을 시행한다(균등한 CPU 분배 목적).
3. 프로세스나 스레드가 자발적으로 CPU를 반환하는 경우 CPU 스케줄링이 시행된다(자발적 CPU 양보).
4. 현재 실행중인 프로세스나 스레드보다 더 높은 순위의 프로세스나 스레드로부터 내려진 입출력이 완료되어 I/O 인터럽트가 발생한 경우, 인터럽트 서비스 루틴에서 I/O를 기다렸던 프로세스나 스레드를 깨우고 스케줄링한다(우선 순위를 지키기 위한 목적).

<br>

> 선점 스케줄링(Preemptive) VS 비선점 스케줄링(Non-Preemptive)

* 선점 스케줄링(Preemptive)
  * 선점(preemption)이란 커널이 현재 실행 중인 프로세스나 스레드를 강제로 중단시키는 행위이다. 
  * 선점 스케줄링은 커널이 실행 중인 프로세스나 스레드를 강제로 중간시켜 준비 리스트로 이동시키고, 스케줄링을 통해 다른 프로세스나 스레드에게 CPU를 넘겨주는 방식이다.
  * 발생 상황
    * 타임 슬라이스(time slice)가 소진되어 타이머 인터럽트가 발생할 때
    * 인터럽트나 시스템 호출 종료 시점에서 더 높은 순위의 프로세스나 스레드가 준비 상태에 있을 때
  * RR(Round Robin), SJF(Shortest Job First), Priority(Preemptive version)
* 비선점 스케줄링(Non-Preemptive)
  * 비선점(non-preemptive)이란, 프로세스나 스레드가 CPU를 할당받아 일단 실행을 시작하면 완료되거나 CPU를 더 이상 사용할 수 없는 상황이 될 때까지, 프로세스나 스레드를 강제로 중단시키지 않는 방식이다.
  * 프로세스나 스레드가 실행 도중 I/O를 요청하여 CPU를 더 이상 사용할 수 없게 되었을 때 비로소, 운영체제는 스케줄링을 통해 다른 프로세스에게 CPU를 할당한다.
  * 발생 상황
    * CPU를 더 이상 사용할 수 없게 된 경우 : I/O block, sleep 등
    * 자발적인 CPU 양보 : yield() 시스템 호출
    * 현재 실행중인 스레드가 종료할 때
  * SRTF(Shortest Remaining Time First), Priority(non-preemptive version)

<br>

> 기아(starvation)와 에이징(aging)

* **프로세스나 스레드가 스케줄링에서 선택되지 못한 채 오랜 시간 동안 준비 리스트에 존재하는 상황**을 기아 혹은 기어 현상이라고 한다.
  * 우선순위를 기반으로 하는 스케줄링 시스템에서, 더 높은 순위의 프로세스가 계속 컴퓨터 시스템에 들어오면 프로세스는 스케줄링에서 선택되지 못한 채 오랜 시간 대기하게 된다.
  * 짧은 프로세스를 우선 실행시키는 알고리즘을 사용하는 경우, 자신보다 짧은 프로세스가 계속 시스템에 들어오면 프로세스는 선택에서 계속 배재되어 기아에 빠지게 된다.
* 기아에 대한 해결책으로 가장 많이 사용되는 것이 에이징(aging) 기법이다.
  * **프로세스가 준비 리스트에 머무르는 시간에 비례하여 프로세스의 우선 순위를 높이는 기법**이다.
  * 프로세스가 오래 기다릴 수는 있지만 언젠가 가장 높은 우선 순위에 도달하는 것이 보장되기 대문에 무한정 준비 리스트에 머무르는 일은 발생하지 않는다.