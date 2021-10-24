public class Main {
    public static void main(String[] args) {
        int data[] = {77, 5, 20, 2, 94};
        int N = data.length;

        Insertion i = new Insertion();
        System.out.print("Insertion Sort: ");
        i.insertionSort(data);
        System.out.println();

        Selection s = new Selection();
        System.out.print("Selection Sort: ");
        s.selectionSort(data);
        System.out.println();

        Bubble b = new Bubble();
        System.out.print("Bubble Sort: ");
        b.bubbleSort(data);
        System.out.println();

        Heap h = new Heap();
        System.out.println("Heap Sort: ");
        h.heapSort(data);
        System.out.println();

        Shell sh = new Shell();
        System.out.println("Shell Sort: ");
        sh.shellSort(data);
        System.out.println();

        Merge m = new Merge();
        Merge.buff = new int[N];
        System.out.println("Merge Sort: ");
        m.mergeSort(data,0, N-1);
        System.out.println();
    }
}
