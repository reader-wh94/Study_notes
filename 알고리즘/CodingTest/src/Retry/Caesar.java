package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/12926

public class Caesar {
    public String solution(String s, int n) {
        String answer = "";

        for(int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);

            if(a >= 'a' && a <= 'z') {
                if(a + n > 'z') answer += (char)(a + n - 26);
                else answer += (char)(a + n);
            } else if (a >= 'A' && a <= 'Z') {
                if(a + n > 'Z') answer += (char)(a + n - 26);
                else answer += (char)(a + n);
            } else answer += (char)(a); // 공백 처리
        }

        return answer;
    }
}
