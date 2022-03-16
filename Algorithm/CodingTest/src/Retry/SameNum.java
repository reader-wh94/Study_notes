package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/12906

import java.util.ArrayList;

public class SameNum {
    public class Solution {
        public ArrayList<Integer> solution(int []arr) {
            ArrayList<Integer> answer = new ArrayList<Integer>();
            int current = 10; // arr의 범위는 0~9까지

            for(int i = 0; i < 10; i++) {
                if(arr[i] != current) {
                    answer.add(arr[i]);
                    current = arr[i];
                }
            }
            return answer;
        }
    }
}
