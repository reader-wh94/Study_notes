package Programmers.level1;
import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/12933

public class Desc {
    public long solution(long n) {
        long answer = 0;
        String ans = Long.toString(n); // n을 문자열로 변환
        char [] arr = ans.toCharArray(); // 문자열을 배열로 변환

        Arrays.sort(arr); // 문자열 오름차순 정렬
        ans = new StringBuilder(new String(arr)).reverse().toString(); // 배열 내림차순 정렬, 하나의 문자열로 변환

        answer = Long.parseLong(ans); // 문자열을 long 타입으로 변환
        return answer;
    }
}
