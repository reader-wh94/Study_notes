public class Shell {
    public void shellSort(int[] data) {
        int size = data.length;
        int temp;
        int gap = size;

        for(; gap > 1;) {
            gap = (gap / 3) + 1;
            System.out.println("gap: " + gap);
            for(int i = 0; i < gap; i++) {
                // 삽입 정렬
                for(int j = i + gap; j < size; j+= gap) {
                    // i : gap으로 나눈 묶음을 구분
                    // j : 삽입 정렬 종료 인덱스
                    for(int x = i; x < j; x += gap) {
                        if(data[x] > data[j]) {
                            temp = data[x];
                            data[x] = data[j];
                            data[j] = temp;
                        }
                    }
                }
            }
        }

        for(int i=0; i < size; i++) {
            System.out.print(data[i] + " ");
        }
    }
}
