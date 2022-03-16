package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12935

import java.util.Arrays;

public class Min {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1];
        int min = arr[0];

        if(arr.length < 2) {
            int[] ans = {-1};
            return ans;
        }

        for(int i = 1; i < arr.length; i++) {
            if(min > arr[i]) {
                min = arr[i];
            }
        }

        int idx = 0; // idx 말고 answer[j] = arr[j] 를 사용할 경우 중간에 공백이 생겨 런타임 오류가 발생한다.
        for(int j = 0; j < arr.length; j++) {
            if(arr[j] != min) {
                answer[idx++] = arr[j];
            }
        }

        return answer;
    }
}
