package data_structure.queue;
import java.util.Queue;
import java.util.LinkedList;

public class QueueExample_lib {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<Integer>();

        queue.offer(1); // 순차보관
        queue.offer(2);
        System.out.println(queue.peek()); // 가장 먼저 보관한 값 단순 참조, 큐에서 꺼내지 않음
        queue.offer(5);
        queue.offer(8);

        while(!queue.isEmpty()) {
            System.out.print(queue.poll()+" "); // 가장 먼저 보관한 값 참조, 큐에서 꺼냄
        }
        System.out.println();
        System.out.println(queue.peek());
    }
}
