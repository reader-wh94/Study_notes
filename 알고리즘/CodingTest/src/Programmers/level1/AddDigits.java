package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12931

public class AddDigits {
    public int solution(int n) {
        int answer = 0;
        while(n != 0) {
            answer += n % 10;
            n /= 10;
        }

        return answer;
    }
}
