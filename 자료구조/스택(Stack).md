## 스택(Stack)

---

### 스택의 구조

<img src="D:\Study\Study_notes\사진\스택 구조.PNG" style="zoom: 67%;" />

<br>

### 스택의 특징

* 스택의 입출력은 맨 위에서만 일어나고 스택의 중간에서는 데이터를 삭제할 수 없다.
* **LIFO (Last-In-Fisrt-Out)**의 형태를 가지고 있다.
  * A -> B -> C -> D의 순서로 스택에 삽입되었을 경우 삭제 순서는 D -> C -> B -> A가 된다.
* 스택의 가장 위를 top이라고 하며 top 에서 삽입과 삭제가 이루어진다.
* 스택에 요소가 하나도 없을 때 그러한 스택을 **공백 스택(empty stack)**이라고 한다.

<br>

### 스택의 연산

* push: 스택에 새로운 원소를 삽입
* pop: 스택의 top 원소를 제거하고 반환
* empty: 스택이 비어있는지 검사
* size: 스택의 크기
* swap: 두 스택의 내용을 바꿈
* top: top에 있는 원소를 반환

<br>

### 스택 구현 코드

```c++
#include <iostream>
#include <stack>

using namespace std;

int main() {
	// 스택 생성
	stack<int> s;

	// 10, 20, 30 순서로 삽입
	s.push(10);
	s.push(20);
	s.push(30);

	cout << "top element: " << s.top() << "\n";
	
	//상단 2개 삭제
	s.pop();
	s.pop();

	cout << "size: " << s.size() << "\n";
	cout << "top: " << s.top() << "\n";
	cout << "empty: " << (s.empty() ? "YES" : "NO") << "\n";

	return 0;
}
```

