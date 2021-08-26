#include <iostream>

using namespace std;

void shellSort(int arr[], int len) {
	int i, j, temp;
	int gap = len / 2;
	while (gap > 0) {
		for (i = gap; i < len; i++) {
			temp = arr[i];
			j = i;
			while (j >= gap && arr[j - gap] > temp) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			arr[j] = temp;
		}
		gap /= 2;
	}
}

int main() {
	int arr[] = { 10,8,6,20,4,3,22,1,0,15,16 };
	int len = sizeof(arr) / sizeof(int);

	cout << "정렬 전: ";
	for (int x : arr)
		cout << x << " ";
	cout << endl;

	shellSort(arr, len);

	cout << "정렬 후: ";
	for (int x : arr)
		cout << x << " ";
	cout << endl;
}