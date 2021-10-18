public class Insertion {
    int i, j;
    int temp;
    int []a = {7, 2, 3, 9, 1};

    public void insertionSort() {
        for(i = 1; i < a.length; i++) {
            int standard = a[i];
            j = i - 1; // j는 정렬이 끝난 끝 지점을 가리킴

            while(j >= 0 && standard < a[j]) {
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = standard;
        }

        for(i=0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
