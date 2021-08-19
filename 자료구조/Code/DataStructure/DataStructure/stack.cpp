#include <iostream>
#include <stack>

using namespace std;

int main() {
	// ���� ����
	stack<int> s;

	// 10, 20, 30 ������ ����
	s.push(10);
	s.push(20);
	s.push(30);

	cout << "top element: " << s.top() << "\n";
	
	//��� 2�� ����
	s.pop();
	s.pop();

	cout << "size: " << s.size() << "\n";
	cout << "top: " << s.top() << "\n";
	cout << "empty: " << (s.empty() ? "YES" : "NO") << "\n";

	return 0;
}