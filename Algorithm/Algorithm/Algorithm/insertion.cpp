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