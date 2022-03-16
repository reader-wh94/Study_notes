package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12918

public class FindNumber {
    public boolean solution(String s) {
        boolean answer = true;

        if(s.length() == 4 || s.length() == 6) { // 문자열 s의 길이가 4 혹은 6이라는 조건이 있었다. 문제를 꼼꼼히 읽을 것
            if(s.matches(".*[a-zA-Z].*")) {
                answer = false;
            } else {
                answer = true;
            }
        } else answer = false;

        return answer;
    }
}