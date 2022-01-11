package Programmers.level2;

// https://programmers.co.kr/learn/courses/30/lessons/12939

import java.util.ArrayList;
import java.util.Collections;

public class MaxNMin {
    public String solution(String s) {
        String answer = "";

        String[] arr = s.split(" ");
        ArrayList<Integer> arr2 = new ArrayList<Integer>();

        for(int i = 0; i < arr.length; i++) {
            arr2.add(Integer.parseInt(arr[i]));
        }

        Collections.sort(arr2);
        answer += arr2.get(0);
        answer += " ";
        answer += arr2.get(arr.length - 1);

        return answer;
    }
}
