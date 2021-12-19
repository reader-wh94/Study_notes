package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/42576

import java.util.HashMap;

public class Marathon {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for(String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        for(String c: completion) {
            map.put(c, map.get(c) - 1);
        }

        for(String ans: map.keySet()) {
            if(map.get(ans) != 0) {
                answer = ans;
            }
        }

        return answer;
    }
}
