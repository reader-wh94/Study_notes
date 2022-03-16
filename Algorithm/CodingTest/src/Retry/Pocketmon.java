package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/1845

import java.util.HashSet;

public class Pocketmon {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length / 2;

        HashSet<Integer> set = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++) { // HashSet으로 중복을 제거
            set.add(nums[i]);
        }

        if(set.size() < n) {
            answer = n;
        } else {
            answer = set.size();
        }
        return answer;
    }
}

// HashSet이랑 HashMap이랑 헷갈렸다 (사실 HashSet을 이번에 공부하면서 다시 배움)
