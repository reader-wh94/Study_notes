package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/86051

public class Exist {
    public int solution(int[] numbers) {
        int answer = -1;
        int sum = 45;

        for(int i = 0; i < numbers.length; i++) {
            sum -= numbers[i];
        }

        answer = sum;
        return answer;
    }
}
