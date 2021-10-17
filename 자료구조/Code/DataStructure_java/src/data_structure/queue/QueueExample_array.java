package data_structure.queue;

public class QueueExample_array {
    int MAX = 1000;
    int front;
    int rear;
    int [] queue;

    public QueueExample_array() { // 큐 생성 및 초기화
        front = rear = 0;
        queue = new int[MAX];
    }

    public boolean queueisEmpty() {
        return front == rear;
    }

    public boolean queueisFull() {
        if(rear == MAX - 1) {
            return true;
        } else
            return false;
    }

    public void offer(int value) {
        if(queueisFull()) {
            System.out.println("Queue is Full");
            return;
        }
        queue[rear++] = value; // rear가 위치한 곳에 값을 넣고 rear를 증가
    }

    public int poll() {
        if(queueisEmpty()) {
            System.out.println("Queue is Empty");
            return -1;
        }
        int popValue = queue[front++]; // 반환 값에 front 값을 넣고 front 증가
        return popValue;
    }

    public int peek() {
        if(queueisEmpty()) {
            System.out.println("Queue is Empty");
            return -1;
        }
        int peekValue = queue[front];
        return peekValue;
    }
}

class Main {
    public static void main(String[] args) {
        QueueExample_array queue = new QueueExample_array();
        queue.offer(1);
        queue.offer(4);
        queue.offer(8);
        queue.offer(9);

        System.out.println("Peek: " + queue.peek());

        queue.poll();
        queue.poll();

        while(!queue.queueisEmpty()) {
            System.out.print(queue.poll()+" ");
        }
    }
}