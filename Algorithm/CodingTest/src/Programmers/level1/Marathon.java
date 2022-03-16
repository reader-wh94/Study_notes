package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/42576

import java.util.HashMap;

public class Marathon {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>(); // key 값을 이름으로 설정, value는 카운트

        for(String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
            // p가 map에 있으면 value를 가져오고 아닐 경우 0을 default 값으로 설정
        }

        for(String c : completion) {
            map.put(c, map.get(c) - 1);
        }

        for(String ans : map.keySet()) {
            if(map.get(ans) != 0) {
                answer = ans;
            }
        }
        return answer;
    }
}

// 참고 : https://coding-grandpa.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98-%ED%95%B4%EC%8B%9C-Lv-1
// HashMap에서 getOrDefault라는 함수가 있는 지 몰랐다...