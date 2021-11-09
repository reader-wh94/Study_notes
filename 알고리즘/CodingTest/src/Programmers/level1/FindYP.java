package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12916

public class FindYP {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;

        if(s.length() > 51) {
            answer = false;
        } else {
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                    p++;
                } else if(s.charAt(i) == 'y' || s.charAt(i) == 'Y'){
                    y++;
                }
            }
            if(p != y) answer = false;
        }

        return answer;
    }
}
