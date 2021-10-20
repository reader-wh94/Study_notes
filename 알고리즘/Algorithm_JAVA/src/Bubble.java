public class Bubble {
    public void bubbleSort(int[] data) {
        int i,j,temp;
        int size = data.length;

        for(i=0; i < size; i++) {
            for(j=0; j < size - i - 1; j++) {
                if(data[j] > data[j+1]) {
                    temp = data[j+1];
                    data[j+1] = data[j];
                    data[j] = temp;
                }
            }
        }

        for(int k = 0; k < size; k++) {
            System.out.print(data[k] + " ");
        }
    }
}
