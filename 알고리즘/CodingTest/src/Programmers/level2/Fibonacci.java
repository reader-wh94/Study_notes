package Programmers.level2;

// https://programmers.co.kr/learn/courses/30/lessons/12945

public class Fibonacci {
    public int solution(int n) {
        int answer = 0;
        int n1 = 1;
        int n2 = 1;

        if(n == 1 || n == 2) return 1;
        else {
            for(int i = 3; i <= n; i++) {
                answer = (n1 + n2) % 1234567;
                n1 = n2; // n - 1
                n2 = answer; // n - 2
            }
            return answer;
        }
    }
    /* public int fibonacci(int n) {
        if(n <= 1) {
            return n;
        } else {
            return ((fibonacci(n-1) % 1234567) + (fibonacci(n-2) % 1234567)) % 1234567;
        } // (A + B) % C == ((A % C) + (B % C)) % C
    } */
    // 재귀로 피보나치를 풀면 메모리 차지가 많아진다
}
