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