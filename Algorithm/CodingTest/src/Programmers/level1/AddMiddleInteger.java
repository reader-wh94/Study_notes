package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12912

public class AddMiddleInteger {
    public long solution(int a, int b) {
        long answer = 0;
        int min = Math.min(a, b); // 최댓값과 최솟값은 Math를 사용
        int max = Math.max(a, b);

        if(a == b) {
            answer = a;
        } else {
            for(int i = min; i <= max; i++) {
                answer += i;
            }
        }

        return answer;
    }
}
