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

/*
*   동명이인이 있기 때문에 <String, Integer>로 해결해야한다. <Integer, String>이 아님!
*   map.getOrDefault 함수를 통해 만약 해당 사람이 이미 해쉬맵에 있다면(동명이인) value을 +1 하거나 -1 한다.
*   결국 key 값 전체를 검사하여 해당 키의 value 값이 0인 사람을 찾아 return 한다.
* */