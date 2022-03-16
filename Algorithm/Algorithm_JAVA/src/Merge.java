import java.util.Arrays;

public class Merge {
    public static int[] buff;

    public void merge(int[] data, int m, int mid, int n) {
        int i = m;
        int j = mid + 1;
        int k = m;

        while(i <= mid && j <= n) {
            if(data[i] <= data[j]) {
                buff[k] = data[i++];
            } else {
                buff[k] = data[j++];
            }
            k++;
        }

        if(i > mid) {
            for(int p = j; p <= n; p++, k++) {
                buff[k] = data[p];
            }
        } else {
            for(int p = i; p <- mid; p++, k++) {
                buff[k] = data[p];
            }
        }

        for(int p = m; p <= n; p++) {
            data[p] = buff[p];
        }
    }

    public void print(int[] data) {
        for(int i=0; i < data.length; i++) {
            System.out.print(data[i] + " ");
        }
    }

    public void mergeSort(int[] data, int m, int n) {
        int mid;
        if(m < n) {
            mid = (m+n)/2;
            mergeSort(data, m, mid);
            mergeSort(data, mid+1, n);
            merge(data, m, mid, n);
        }
    }
}
