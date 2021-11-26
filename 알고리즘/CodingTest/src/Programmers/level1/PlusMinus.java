package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/76501

public class PlusMinus {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 123456789;
        int sum = 0;

        for(int i = 0; i  < signs.length; i++) {
            if(signs[i]) sum += absolutes[i];
            else sum -= absolutes[i];
        }

        answer = sum;

        return answer;
    }
}
