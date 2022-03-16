## 선택 정렬(Selection Sort)

----

### 선택 정렬

* 배열에서 최소값을 발견한 다음, 이 최소값을 배열의 첫번째 요소와 교환한다.
* 다음에는 첫번째 요소를 제외한 나머지 요소들 중에서 가장 작은 값을 선택하고 이를 두번째 요소와 교환한다.
* 이 절차를 (개수 - 1)만큼 되풀이한다.

<br>

### 선택 정렬의 과정

![선택 정렬](https://user-images.githubusercontent.com/68210266/130445203-67b4e060-8888-43d9-942e-bc39acff39f5.PNG)

<br>

### 구현 코드

```c++
#include <iostream>

using namespace std;

void swap(int& a, int& b) {
	int tmp;
	tmp = a;
	a = b;
	b = tmp;
}

void SelectionSort(int* arr, int len) {
	int min_idx;
	for (int i = 0; i < len - 1; i++) {
		min_idx = i;

		for (int j = i + 1; j < len; j++) {
			if (arr[min_idx] > arr[j]) {
				min_idx = j;
			}
		}
		swap(arr[min_idx], arr[i]);
	}
}

int main(void) {
	int arr[6] = { 5,3,8,1,2,7 };
	int len = 6;

	for (int i = 0; i < len; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;

	SelectionSort(arr, len);

	for (int i = 0; i < len; i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
```

<br>

### 시간 복잡도

- (n-1) + (n-2) + .... + 1 = n(n-2)/2 = O(n^2)

![시간 복잡도](https://user-images.githubusercontent.com/68210266/130449509-fa9aa4b1-29be-4fcf-9dbc-b6062fbc5a93.PNG)

<br>

[코드 참고](https://blockdmask.tistory.com/153)