#include <iostream>
#include <queue>
using namespace std;

int main() {
	// ť ����
	queue<int> q;

	// ������ ����
	q.push(10);
	q.push(20);
	q.push(30);
	q.push(40);
	q.push(50);

	// ������ ����
	q.pop();
	q.pop();
	q.pop();

	// front �ٷ�
	cout << "front element: " << q.front() << "\n";

	// rear ���
	cout << "rear element: " << q.back() << "\n";

	// size ���
	cout << "queue size: " << q.size() << "\n";

	// empty 
	cout << "empty? :" << (q.empty() ? "YES" : "NO") << "\n";
}