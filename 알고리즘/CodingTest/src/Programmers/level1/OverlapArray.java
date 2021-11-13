package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12906

import java.util.ArrayList;

public class OverlapArray {
    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int current = 10; // current는 0~10까지이므로 arr[0]이 뭐든 간에 if문에 해당

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != current) {
                answer.add(arr[i]);
                current = arr[i]; // arr[i+1] (다음 원소)랑 비교하기 위해 current를 arr[i]로 설정한다
            }
        }
        return answer;
    }
}

// for문으로 i와 j(i + 1) 끼리 비교하여 값이 같으면 arr[i]를 answer에 저장,
// 값이 달라도 arr[i]를 저장하는 로직을 구현하고
// 만약 answer의 마지막 원소가 arr[i]와 같을 경우 (ex. {1,2,3,3,4} 에서 3,4를 비교했는데 answer 마지막 원소가 3일 경우)
// answer의 마지막 값을 제거하고 arr[i]를 다시 저장하는 로직을 구현했으나 index 관련 오류가 해결이 잘 안됐다
// 디버깅 더 돌려보고 노력하면 수정이 가능 했을텐데 시간이 없어서 current를 써서 해결하는 방법으로 변경했다.