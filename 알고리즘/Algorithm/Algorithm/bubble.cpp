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