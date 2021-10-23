#include <iostream>

using namespace std;
int a[10] = { 27,10,12,20,25,13,15,22,8,2 };

void m_sort(int list[], int l, int m, int r) {
	int i, j, k;
	i = l;
	j = m + 1;
	k = l;
	int temp[11];

	while (i <= m && j <= r) {
		if (list[i] <= list[j])
			temp[k++] = list[i++];
		else
			temp[k++] = list[j++];
	}

	if (i > m) {
		for (int x = j; x <= r; x++)
			temp[k++] = list[x];
	}
	else {
		for (int x = i; x <= m; x++)
			temp[k++] = list[x];
	}

	for (int x = l; x <= r; x++)
		list[x] = temp[x];
}

void merge(int list[], int l, int r) {
	int mid;
	if (l < r) {
		mid = (l + r) / 2;
		merge(list, l, mid);
		merge(list, mid + 1, r);
		m_sort(list, l, mid, r);
	}
}
int main() {
	merge(a, 0, 9);
	for (int i = 0; i < 10; i++) {
		cout << a[i] << " ";
	}
	return 0;
}