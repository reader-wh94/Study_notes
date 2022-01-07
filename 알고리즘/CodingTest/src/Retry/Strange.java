package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/12930

public class Strange {
    public String solution(String s) {
        String answer = "";

        String[] words = s.split(" ", -1);
        // limit 값을 음수로 주면 모든 구분 값을 나눠서 배열로 반환한다.

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

        answer = answer.substring(0, answer.length() - 1);
        // answer 마지막에 " " 이 있으므로 제거하고 answer 반환
        return answer;
    }
}
