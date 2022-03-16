#include <iostream>
#include <vector>
using namespace std;

int arr[7] = { 38, 27, 43, 9, 3, 82, 10 };

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
    for (const int& n : arr) cout << n << ' ';
}

int main() {
    quick_sort(0, 6);
    print();

    return 0;
}