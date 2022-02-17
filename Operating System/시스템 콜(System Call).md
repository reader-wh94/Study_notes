##  시스템 콜(System Call)

> 시스템 콜(system call)

![system call 1](https://user-images.githubusercontent.com/68210266/154472236-72d7b46c-8fa3-4b49-81e2-e3c7809898b4.PNG)

<br>

응용 프로그램은 함수 호출(function call)을 통해 다른 함수들을 실행한다. 하지만 응용 프로그램은 커널에 있는 함수를 함수 콜(system call)의 방법으로 호출할 수 없다. 왜냐하면, 커널 코드 안에 들어 있는 함수의 이름을 알 수도 없을 뿐더러, 설사 안다고 하더라도 응용 프로그램이 커널 코드와 링크할 수 없기 때문이다.

응용 프로그램에서 커널에 작성된 함수를 호출하는 다른 방법이 제공되는데, 그것이 바로 시스템 콜(system call)이다.

<br>

> 시스템 콜(system call)의 유형

### 1. fork()

* 현재 프로세스와 동일하게 생긴 자식 프로세스를 만든다.

* fork()는 코드 ,데이터, 스택, 힙 등 부모 프로세스와 완벽히 동일한 자식 프로세스를 만들고 리턴한다. 그러므로 두 프로세스 모두 fork()에서 리턴한 후, 동일한 주소에서 각자 실행을 시작한다.
* 부모와 자식 프로세스는 단 한 가지에서 다른 점을 가진다. fork() 시스템 호출이 자식 프로세스를 생성하고 리턴할 때, 부모 프로세스에게는 막 생성한 자식 프로세스의 PID 값을 전달하고, 자식 프로세스에게는 0을 전달한다.

```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
    pid_t pid;
    int status, i, sum;
    
    pid = fork(); /* 자식 프로세스 생성*/
    
    if(pid > 0) { /*부모 프로세스에 의해 실행되는 코드*/
        printf("parent: fork()의 리턴 값 = 자식 프로세스 pid = %d \n", pid);
        printf("parent: 프로세스 pid = %d \n", getpid());
        sleep(1); // 1초 후에 종료
        return 0;
    }
    else if(pid == 0) { /*자식 프로세스에 의해 실행되는 코드*/
        printf("child: fork()의 리턴 값 pid = %d \n", pid);
        printf("child: 프로세스 pid = %d, 부모 프로세스 pid = %d \n", getpid(), getppid());
        
        sum = 0;
        for(int i = 0; i < 100; i++) {
            sum += i;
        }
        printf("child: sum = %d \n", sum);
        return 0;
    }
    else { /*fork() 오류*/
        fprintf(stderr, "fork error");
        return 1;
    }
}
```

결과

```bash
parent: fork()의 리턴 값 = 자식 프로세스 = 15747
parent: 프로세스 pid = 15746
child: fork()의 리턴 값 pid = 0
child: 프로세스 pid = 15747, 부모 프로세스 pid = 15746
child: sum = 4950
```

<br>

<br>

### 2. exec()

* 현재 실행중인 프로세스의 컨텍스트(context)에 새로운 실행 파일로부터 응용프로그램을 로딩하여 실행시킬 때 사용되는 기법이다.

* 자신의 주소 공간에 새로운 응용프로그램의 코드, 데이터, 스택, 힙을 올리게 되어 현재 프로세스의 모든 정보들이 삭제된다.

<br>

<br>

### 3. wait()

* 자식 프로세스가 종료될 때까지 기다리는 작업이다.

<br>

출처: [Tech Interview](https://gyoogle.dev/blog/computer-science/operating-system/System%20Call.html)