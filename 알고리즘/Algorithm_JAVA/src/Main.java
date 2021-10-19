public class Main {
    public static void main(String[] args) {
        int data[] = {77, 5, 20, 2, 94};

        Insertion i = new Insertion();
        System.out.print("Insertion Sort: ");
        i.insertionSort(data);
        System.out.println();

        Selection s = new Selection();
        System.out.print("Selection Sort: ");
        s.selectionSort(data);
        System.out.println();
    }
}
