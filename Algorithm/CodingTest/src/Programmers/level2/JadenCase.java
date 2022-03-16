package Programmers.level2;

// https://programmers.co.kr/learn/courses/30/lessons/12951

public class JadenCase {
    public String solution(String s) {
        String answer = "";
        String[] sp = s.toLowerCase().split("");

        boolean flag = true; // 첫 글자는 항상 대문자

        for(String str : sp) {
            answer += flag ? str.toUpperCase() : str; // flag == true 이면 대문자로
            flag = str.equals(" ")? true : false; // flag가 공백일 경우 flag == true로 변경
        }
        return answer;
    }
}

// 코드 참고: https://hj-bank.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-JadenCase-JAVA