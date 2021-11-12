package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12917

import java.util.Arrays;
import java.util.Collections;

public class SortString {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();

        Arrays.sort(arr);
        return new StringBuilder(new String(arr)).reverse().toString();
        // StringBuilder를 사용하여 reverse하기
    }
}
