## 퀵 정렬(Quick Sort)

---

### 퀵 정렬

* 분할-정복법(divide and conquer)에 근거한다.
* 퀵정렬은 합병 정렬과 비슷하게 전체 리스트를 2개의 부분 리스트로 분할하고, 각각의 부분 리스트를 다시 퀵정렬하는 전형적인 분할-정복법을 사용한다.
* 합병 정렬과의 다른 점은 리스트를 비균등하게 분할한다는 점이다.
* 리스트 안의 한 요소를 피벗(pivot)으로 선택하면 피벗보다 작은 요소들은 피벗의 왼쪽으로, 피벗보다 큰 요소들은 피벗의 오른쪽으로 옮겨진다.
* 이 상태에서 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬하게 되면 전체 리스트가 정렬된다.
* 합병 정렬과 마찬가지로 부분 리스트에 대해 순환 호출된다.

<br>

### 퀵 정렬의 과정

![quick](https://user-images.githubusercontent.com/68210266/138637362-a903a9e1-1c13-4993-a0d4-737488e28252.png)

* 피벗을 5로 설정한 후, 5보다 작은 값은 왼쪽 리스트에, 큰 값은 오른쪽 리스트로 보내는 탐색과 교환 과정을 반복한다.
* low와 high 포인터가 서로 엇갈리게 되면 멈춘 후 피벗을 중앙으로 이동시켜 피벗을 기준으로 2개의 리스트로 나뉘어진다.
* 각 왼쪽, 오른쪽 리스트 별로 위와 같은 과정(pivot 설정 후 탐색-교환 과정)을 반복한다.

<br>

### 전체 과정

![quick2](https://user-images.githubusercontent.com/68210266/138637394-8ce44034-6884-44c7-8ca4-4da544a2b231.jpg)

<br>

### 구현 코드

```c++
#include <iostream>
using namespace std;

int arr[7] = {38, 27, 43, 9, 3, 82, 10};

void quick_sort(int start, int end) {
  if (start >= end) return;
  int pivot = start; 
  int low = start + 1, high = end;

  while (low <= high) {
    while (arr[low] <= arr[pivot] && low <= end) low++;
    while (arr[high] >= arr[pivot] && high > start) high--;

    if (low > high) 
      swap(arr[pivot], arr[high]);
    else 
      swap(arr[low], arr[high]);
  }

  quick_sort(start, high - 1);
  quick_sort(high + 1, end);
}


void print() {
  for (const int &n : arr) cout << n << ' ';
}

int main() {
  quick_sort(0, 6);
  print();

  return 0;
}
```

<br>

### 시간복잡도

* n개의 레코드를 가지는 리스트는 n/2, n/4, n/8 ... n/2^k의 크기로 나누어 질 것이다.  크기가 1이 될 때까지 나누어지므로 n/2^k = 1일 때 까지 나누어진다. 즉 k = log * n개의 패스가 필요하다.
* 각각의 패스에서 전체 리스트의 대부분의 레코드를 비교해야 하므로 평균 n번 정도의 비교가 이루어진다. 퀵 정렬은 비교 연산을 총 nlogn번 실행하게 되어 O(nlogn)의 복잡도를 가진다.
* 최악의 경우 리스트가 계속 불균형하게 나누어져 패스의 개수는 n, 한 번의 패스에서 평귱 n 번 정도의 비교 연산이 이루어지는 경우 O(n^2)의 시간 복잡도가 된다.

![시간 복잡도](https://user-images.githubusercontent.com/68210266/138639475-55bc58e9-815f-4e41-83bf-0c4495941d5e.PNG)

[코드 참고](https://donggoolosori.github.io/2021/01/05/quicksort/)