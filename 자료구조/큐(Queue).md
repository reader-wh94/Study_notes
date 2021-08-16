## 큐(Queue)

----

### 큐의 구조

![](D:\Study\Study_notes\사진\큐 구조.PNG)

<br>

### 큐의 특징

* 큐는 뒤에서 새로운 데이터가 추가되고 앞에서 데이터가 하나씩 삭제되는 구조를 가지고 있다.
* FIFO(First-In First-Out): 먼저 들어온 데이터가 먼저 나가는 구조이다
  * A -> B -> C -> D의 순서로 큐에 삽입되었을 때 삭제 순서는 A -> B -> C -> D 이다.
* 큐에서 삽입이 일어나는 곳을 후단(Rear)라고 하며 삭제가 일어나는 곳을 전단(Front)라 한다.
* 스택과 다른 점은 삽입과 삭제가 다른 쪽에서 일어난다는 점이다.

<br>

### 큐의 연산

* push(): 큐에 원소를 추가(rear)
* pop(): 큐에 있는 원소를 삭제(front)
* front(): 큐 제일 앞에 있는 원소를 반환
* back(): 큐 제일 뒤에 있는 원소를 반환
* empty(): 큐가 비어 있으면 true, 아니면 false를 반환
* size(): 큐 사이즈를 반환

<br>

### 큐 구현 코드

```c++
#include <iostream>
#include <queue>
using namespace std;

int main() {
	// 큐 생성
	queue<int> q;

	// 데이터 삽입
	q.push(10);
	q.push(20);
	q.push(30);
	q.push(40);
	q.push(50);

	// 데이터 삭제
	q.pop();
	q.pop();
	q.pop();

	// front 줄력
	cout << "front element: " << q.front() << "\n";

	// rear 출력
	cout << "rear element: " << q.back() << "\n";

	// size 출력
	cout << "queue size: " << q.size() << "\n";

	// empty 
	cout << "empty? :" << (q.empty() ? "YES" : "NO") << "\n";
}
```

