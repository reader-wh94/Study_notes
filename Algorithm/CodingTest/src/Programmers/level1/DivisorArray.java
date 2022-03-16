package Programmers.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

// https://programmers.co.kr/learn/courses/30/lessons/12910

public class DivisorArray {
    public ArrayList<Integer> solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] % divisor == 0) {
                answer.add(arr[i]);
            }
        }
        if(answer.isEmpty()) {
            answer.add(-1);
        }
        Collections.sort(answer);
        return answer;
    }
}
