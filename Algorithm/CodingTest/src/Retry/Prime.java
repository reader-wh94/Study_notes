package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/12921

public class Prime {
    public int solution(int n) {
        int answer = 0;

        for(int i = 2; i <= n; i++) {
            for(int j = 2; j <= i; j++) {
                if(j == i) answer++;
                else if (i % j == 0) break;
            }
        }

        System.out.println(answer);
        return answer;
    }
}
