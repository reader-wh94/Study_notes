package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12954

public class Increase {
    public long[] increase(int x, int n) {
        long[] answer = new long[n];
        long increase = x; // int로 하는 경우 13, 14번 테스트 케이스에서 실패가 뜬다!

        for(int i = 0; i < n; i++) {
            answer[i] = increase;
            increase += x;
        }

        return answer;
    }
}
