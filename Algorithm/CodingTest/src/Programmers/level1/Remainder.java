package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/87389

import java.util.*;

public class Remainder {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i = 1; i < n; i++) {
            if(n % i == 1) {
                arr.add(i);
            }
        }

        answer = Collections.min(arr);

        return answer;
    }
}
