public class Selection {
    public void selectionSort(int[] data) {
        int size = data.length;
        int minIdx, temp;

        for(int i = 0; i < size - 1; i++) {
            minIdx = i; // 정렬되지 않은 곳을 시작 위치로 지정

            for(int j=i+1; j < size; j++) {
                if(data[j] < data[minIdx]) {
                    minIdx = j;
                }
            }

            temp = data[minIdx];
            data[minIdx] = data[i];
            data[i] = temp;
        }

        for(int i = 0; i < size; i++) {
            System.out.print(data[i] + " ");
        }
    }
}
