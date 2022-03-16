package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/12915

import java.util.ArrayList;
import java.util.Collections;

public class StringSort {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];

        ArrayList<String> arr = new ArrayList<String>();

        for(int i = 0; i < strings.length; i++) {
            arr.add(strings[i].charAt((n)) + strings[i]);
        }

        Collections.sort(arr);

        for(int i = 0; i < strings.length; i++) {
            answer[i] = arr.get(i).substring(1);
        }

        return answer;
    }
}
