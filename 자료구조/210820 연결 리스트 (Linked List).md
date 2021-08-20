## 연결 리스트 (Linked List)

### 연결 리스트

* 물리적으로 흩어져 있는 자료들을 서로 연결하여 하나로 묶는 방법을 연결 리스트(Linked List)라고 한다.

* 연결 리스트는 배열의 단점을 보완하고자 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
* 연결 리스트 기본 구조와 용어
  * 노드(Node): 데이터 저장 단위(데이터 값, 포인터)로 구성
  * 포인터(Pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

![노드 구조](https://user-images.githubusercontent.com/68210266/130233821-d0e2911d-df43-481d-b7c5-65e22b8f8eb1.PNG)

* 3가지 종류의 연결 리스트가 있다
  * 단순 연결 리스트
  * 원형 연결 리스트
  * 이중 연결 리스트

![연결 리스트 종류](https://user-images.githubusercontent.com/68210266/130236274-e4713cbc-1ffb-4f6d-ac1d-e49daff31b9b.PNG)

<br>

### 단순 연결 리스트 구현

* 구조

```c++
typedef struct ListNode {
	int data;
	struct ListNode* next;
} ListNode;
```

​	구조체 내부에 데이터를 저장하는 data와 다음 노드의 주소를 가리키는(저장하는) next 변수가 있다.

```c++
ListNode* head = NULL;
```

​	또한 연결 리스트의 처음을 가리키는 head(헤드 포인터)라는 변수가 있다. 데이터에 접근하려면 이 변수를 통	해서 접할 수 있다.



* 데이터 삽입

  데이터는 리스트의 처음 또는 원하는 위치에 삽입할 수 있다. head에 데이터가 없다면 가장 처음에 데이터가 삽입되고, 데이터가 있다면 인자로 전달된 position의 위치에 노드가 삽입된다. 데이터의 길이보다 position이 더 크다면 리스트의 가장 마지막에 노드가 삽입된다.

```c++
void InsertInLinkedList(ListNode** head, int data, int position) {
	ListNode* inserted = new ListNode;
	inserted->data = data;

	if (position == 1 || *head == NULL) {
		inserted->next = *head;
		*head = inserted;
	}
	else {
		ListNode* inserted_prev = *head;
		for (int i = 1; (inserted_prev->next != NULL) && (i < position - 1); i++) {
			inserted_prev = inserted_prev->next;
		}

		ListNode* inserted_next = inserted_prev->next;
		inserted_prev->next = inserted;
		inserted->next = inserted_next;
	}
}
```



* 데이터 삭제

head에서 인자 position의 위치에 해당하는 노드를 삭제한다. 삭제하려는 position에 노드가 없으면 가장 마지막 노드를 삭제한다. 

```c++
void DeleteNodeFromLinkedList(ListNode** head, int position) {
	if (*head == NULL) {
		cout << "List empty" << "\n";
		return;
	}
	ListNode* removed_prev;
	ListNode* removed;
	if (position == 1) {
		removed = *head;
		*head = (*head)->next;
		delete(removed);
	}
	else {
		ListNode* removed_prev = *head;
		removed = removed_prev->next;
		for (int i = 1; (removed->next != NULL) && (i < position - 1); i++) {
			removed_prev = removed_prev->next;
			removed = removed_prev->next;
		}
		removed_prev->next = removed->next;
		delete(removed);
	}
}
```



* 데이터 출력

```c++
void PrintList(ListNode* head) {
	ListNode* current = head;
	while (current != NULL) {
		cout << current->data << " -> ";
		current = current->next;
	}
	cout << "NULL\n";
}
```

모든 리스트를 탐색하면서 데이터를 출력하며 head부터 NULL까지 탐색해야한다.

<br>

출처: [1](https://heung-bae-lee.github.io/2020/04/28/data_structure_03/), [2](https://codechacha.com/ko/singly-linked-list-in-cpp/)

