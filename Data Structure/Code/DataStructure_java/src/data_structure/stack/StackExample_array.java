package data_structure.stack;

public class StackExample_array {
    static class Stack {
        int top;
        int[] stack;
        int size;

        public Stack(int size) {
            this.size = size;
            stack = new int[size];
            top = -1; // top 포인터 초기화
        }

        public void push(int item) {
            if (top > size) {
                throw new ArrayIndexOutOfBoundsException();
            }
            stack[++top] = item;
        }

        public int pop() {
            if (top == -1) {
                throw new ArrayIndexOutOfBoundsException();
            }
            return stack[top--];
        }

        public int peek() {
            if (top == -1) {
                throw new ArrayIndexOutOfBoundsException();
            }
            return stack[top];
        }

        public void print() {
            System.out.println("stack list ");
            for (int i = top; i >= 0; i--) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Stack st = new Stack(100);
        st.push(1);
        st.push(2);
        st.push(3);
        st.push(4);
        st.push(5);
        st.print();
        System.out.println("peek: "+st.peek());
        st.pop();
        st.print();
        st.pop();
        st.pop();
        st.pop();
        st.print();
    }
}

