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