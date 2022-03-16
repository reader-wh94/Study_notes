package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12982

import java.util.Arrays;

public class Budget {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int sum = 0;

        Arrays.sort(d);

        for(int i = 0; i < d.length; i++) {
            sum += d[i];
            answer++;

            if(sum > budget) {
                answer = i;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Budget b = new Budget();
        int[] arr = {1, 3, 2, 5, 4};
        b.solution(arr, 10);
    }
}
