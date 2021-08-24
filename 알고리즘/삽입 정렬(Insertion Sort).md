## 삽입 정렬(Insertion Sort)

----

### 삽입 정렬

* 정렬되어 있는 리스트에 새로운 레코드를 적절한 위치에 삽입하는 과정을 반복한다.
* 정렬되어 있지 않은 부분의 첫 번째 숫자가 정렬된 부분의 어느 위치에 삽입되어야 하는가를 판단한 후 해당 위치에 이 숫자를 삽입한다.

<br>

### 삽입 정렬의 과정

![삽입 연성](https://user-images.githubusercontent.com/68210266/130596799-fbcc266e-524c-4166-8a03-321c84cb7f79.PNG)

카드 게임을 할 때, 새로운 카드가 들어오면 새로운 카드를 기존의 카드 사이의 올바른 자리를 찾아 삽입 하는데 그 경우와 똑같다고 생각하면 된다.

<br>

### 구현 코드

```c++
#include <iostream>

using namespace std;

void insertionSort(int arr[], int len) {
	int i, j, temp;

	for (i = 1; i < len; i++) {
		temp = arr[i];
		for (j = i - 1; j >= 0; j--) {
			if (arr[j] < temp)
				break;
			arr[j + 1] = arr[j];
		}
		arr[j + 1] = temp;
	}
}

int main() {
	int arr[6] = { 5,3,8,1,2,7 };
	
	cout << "정렬 전: ";
	for (int x : arr)
		cout << x << " ";
	cout << endl;

	insertionSort(arr, sizeof(arr) / sizeof(int));
	
	cout << "정렬 후: ";
	for (int x : arr)
		cout << x << " ";
}
```

<br>

### 시간 복잡도

* 삽입 정렬의 외부 루프는 n-1번 실행되고 각 단계에서 1번의 비교와 2번의 이동만 이루어지므로총 비교 횟수는 n-1번, 총 이동 횟수는 2(n-1)번이 되어 알고리즘의 시간 복잡도는 O(n)이다.
* 총 비교 횟수
  * 각 단계에서 앞에 놓인 자료들은 전부 한 칸씩 뒤로 이동해야한다.
  * 외부 루프 안의 각 반복마다 i번의 비교가 수행된다.
  * ![삽입 정렬 비교 횟수](https://user-images.githubusercontent.com/68210266/130610804-0e76e63d-d210-4bf4-87c9-ae79fc6f67eb.PNG)

* 총 이동 횟수
  * 외부 루프의 각 단계마다 i+2번의 이동이 이루어진다.
  * ![삽입 정렬 이동 횟수](https://user-images.githubusercontent.com/68210266/130611126-2ccaaf3c-250a-4084-9d69-e08d1dc368f9.PNG)

![시간 복잡도](https://user-images.githubusercontent.com/68210266/130611183-8f0e773c-a511-4631-933d-dd0a1a8ec7fa.PNG)