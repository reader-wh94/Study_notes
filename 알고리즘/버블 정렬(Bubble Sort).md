## 버블 정렬(Bubble Sort)

---

### 버블 정렬

* 인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환하는 비교-교환 과정을 리스트의 왼쪽 끝에서 시작하여 오른쪽 끝까지 진행한다.
* 리스트의 비교-교환 과정(스캔)이 한번 완료되면 가장 큰 레코드가 리스트의 오른쪽 끝으로 이동된다.

<br>

### 버블 정렬의 과정

![버블 정렬](https://user-images.githubusercontent.com/68210266/130803990-60db314c-ab52-4740-854c-93c2f95fda99.jpg)

* 5와 3을 비교하면 5가 더 크므로 서로 교환하고, 다음으로 5와 8을 비교하게 되면 8이 더 크므로 교환 없이 다음 단계로 진행된다.
* 한 번의 스캔에 의해 가장 큰 레코드가 리스트의 오른쪽 끝으로 이동하게 된다.
* 스캔의 실행 횟수는 원칙적으로는 (데이터 개수 - 1)번 만큼 실행되지만 중간에 정렬이 끝났다면 계속 실행하지 않는다.

<br>

### 구현 코드

```c++
#include <iostream>

using namespace std;

void bubbleSort(int arr[], int len) {
	int i, j, temp;

	for (i = 0; i < len; i++) {
		for (j = 0; j < len - (i + 1); j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
}

int main() {
	int arr[6] = { 5,3,8,1,2,7 };
	int len = (sizeof(arr) / sizeof(int));

	cout << "정렬 전: ";
	for (int x : arr)
		cout << x << " ";
	cout << endl;

	bubbleSort(arr, len);

	cout << "정렬 후: ";
	for (int x : arr)
		cout << x << " ";
}
```

<br>

### 시간 복잡도

* 비교 횟수
  * 최선, 평균, 최악이 어떠한 경우에도 항상 일정하다.
  * ![버블 복잡도](https://user-images.githubusercontent.com/68210266/130806936-7f49ba15-371f-4b2d-8543-cf3071206558.PNG)

* 이동 횟수
  * 최악의 경우 입력 자료가 역순으로 정렬되어 있는 경우이다. 이때의 이동 횟수는 비교 연산의 횟수에 3을 곱한 갑이다. 한번의 SWAP (데이터 위치 변경) 함수가 3개의 이동을 포함하고 있기 때문이다.
  * 최선의 경우는 입력 자료가 이미 정렬이 되어 있는 경우이다.

![시간 복잡도](https://user-images.githubusercontent.com/68210266/130807380-bc51f62f-396c-40a1-8e3d-914a41fbb925.PNG)