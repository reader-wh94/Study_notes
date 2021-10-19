public class Insertion {
    int i, j;

    public void insertionSort(int []data) {
        int size = data.length;
        for(i = 1; i < size; i++) {
            int standard = data[i];
            j = i - 1; // j는 정렬이 끝난 끝 지점을 가리킴

            while(j >= 0 && standard < data[j]) {
                data[j+1] = data[j];
                j--;
            }
            data[j+1] = standard;
        }

        for(i=0; i < size; i++) {
            System.out.print(data[i] + " ");
        }
    }
}
