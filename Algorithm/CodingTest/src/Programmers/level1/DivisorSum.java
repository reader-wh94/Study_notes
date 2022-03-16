package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/77884

import java.util.HashMap;
import java.util.Map;

public class DivisorSum {
    public int solution(int left, int right) {
        int answer = 0;
        HashMap <Integer, Boolean> hash = new HashMap<Integer, Boolean>();
        int count = 0;

        for(int i = left; i <= right; i++) {
            count = 0;
            for(int j = 1; j <= i; j++) {
                if(i % j == 0)
                    count++;

                if(count % 2 == 0) {
                    hash.put(i, true);
                } else {
                    hash.put(i, false);
                }
            }

        }

        for(Map.Entry<Integer, Boolean> m : hash.entrySet()) {
            if(m.getValue()) answer += m.getKey();
            else answer -= m.getKey();
        }

        return answer;
    }
}
