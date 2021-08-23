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