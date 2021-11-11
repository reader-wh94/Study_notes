package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12903

public class FindMid {
    public String solution(String s) {
        String answer = "";
        int mid = s.length() / 2;

        if(s.length() % 2 != 0) {
            answer = String.valueOf(s.charAt(mid)); // key Point: 문자열의 인덱스는 0부터 시작한다
        } else {
            answer = String.valueOf(s.charAt(mid-1));
            answer += String.valueOf(s.charAt(mid));
        }
        return answer;
    }
}