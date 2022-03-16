public class Heap {
    public void heapSort(int[] data) {
        int size = data.length;

        for(int i = size/2-1; i >= 0; i--) { // i = tree의 level
            heapify(data, size, i);
        }

        System.out.println("===== max heapify =====");
        for(int i = 0; i < size; i++) {
            System.out.print(data[i] + " ");
        }
        System.out.println();

        for(int i = size-1; i > 0; i--) {
            int temp = data[0];
            data[0] = data[i];
            data[i] = temp;

            heapify(data, size, 0);
        }

        System.out.println("===== sort =====");
        for(int i = 0; i < size; i++) {
            System.out.print(data[i] + " ");
        }
    }

    public void heapify(int[] data, int size, int i) {
        int largest = i; // parent node
        int left = 2*i + 1;
        int right = 2*i + 2;

        if(left < size && data[left] > data[right]) { // left 값이 부모노드 값보다 큰 경우
            largest = left; // 부모노드로 만들기 위해 left 값을 저장
        }

        if(right < size && data[right] > data[left]) { // right 값이 부모노드 값보다 큰 경우
            largest = right; //right 값을 부모노드로 설정
        }

        if(largest != i) { // 자식이 부모보다 큰 값인 경우가 존재 할 때
            int temp = data[i];
            data[i] = data[largest];
            data[largest] = temp;

            heapify(data, size, largest); // 부모노드와 자식노드를 바꾼 것을 기준으로 다시 heapify
        }
    }
}
