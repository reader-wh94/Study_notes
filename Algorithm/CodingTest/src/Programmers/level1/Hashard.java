package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12947

public class Hashard {
    public boolean solution(int x) {
        boolean answer = false;
        int sum = 0;
        int mod = x;

        while(x > 0) {
           sum += x % 10; // 한 자리 수씩 더하기
           x /= 10; // 자릿수 줄이기
        }

        if(mod % sum == 0) {
            answer = true;
        }

        return answer;
    }
}
