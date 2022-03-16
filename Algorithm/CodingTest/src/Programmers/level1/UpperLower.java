package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12930

public class UpperLower {
    public String solution(String s) {
        String answer = "";

        // String[] words = s.split("//s"); -> test 4,5,8,9,11 failed
        String[] words = s.split(" ", -1);

        for(int i = 0; i < words.length; i++) {
            for(int j = 0; j < words[i].length(); j++) {
                char a = words[i].charAt(j);

                if(j % 2 == 0) {
                    if(a >= 'a' && a <= 'z') answer += (char)(a - 32);
                    else answer += a;
                } else {
                    if(a >= 'A' && a <= 'Z') answer += (char)(a + 32);
                    else answer += a;
                }
            }
            answer += " ";
        }

        answer = answer.substring(0, answer.length() -1);

        return answer;
    }
}
