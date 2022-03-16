package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/1845

import java.util.HashSet;

public class Pocketmon {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length / 2;

        HashSet<Integer> arr = new HashSet<Integer>();

        // HashSet으로 중복 값 제거
        for(int i = 0; i < nums.length; i++) {
            arr.add(nums[i]);
        }

        answer = (arr.size() < n) ? arr.size() : n;

        return answer;
    }
}

// https://zzang9ha.tistory.com/179 (코드 참고)
// 조합의 중복을 제거할 생각만 했지 처음부터 중복 값을 없애고 남은 수로 조합의 갯수를 파악할 생각을 하지 못했다.
// HashSet을 쓰면 굉장히 간단하게 나올 수 있었던 답인데 HashSet이 기억이 안나서 for문으로 모든 걸 해결할려고 했다.
// 오늘도 나의 무지함에 눈물 한 방울 흘리며 짜파게티나 끓여먹어야겠다
// 내일 다시 풀어봐야지