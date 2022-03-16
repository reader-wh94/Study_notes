import java.util.Arrays;

public class Quick {
    public void quickSort(int[] data, int start, int end) {
        if (start >= end) return;
        int pivot = start;
        int low = start + 1, high = end;
        int temp;

        while(low <= high) {
            while(low <= high && data[low] < data[pivot]) low++;
            while(high > start && data[high] >= data[pivot]) high--;

            if(low > high) {
                temp = data[high];
                data[high] = data[pivot];
                data[pivot] = temp;
            } else {
                temp = data[low];
                data[low] = data[high];
                data[high] = temp;
            }
        }
        quickSort(data, start, high - 1);
        quickSort(data, high + 1, end);
    }

    public void print(int[] data) {
        for(int i=0; i < data.length; i++) {
            System.out.print(data[i] + " ");
        }
    }
}
