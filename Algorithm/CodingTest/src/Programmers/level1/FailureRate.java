package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/42889

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class FailureRate {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] stageStatus = new int[N + 1];

        for(int s : stages) {
            if(s == N + 1) continue; // 마지막 스테이지를 클리어 했을 경우
            stageStatus[s]++; // 단계 별 클리어 하지 못 한 사람의 수
        }


        HashMap<Integer, Double> fRate = new HashMap<Integer, Double>();
        int len = stages.length;
        for(int i = 1; i <= N; i++) {
            if(len == 0) {
                fRate.put(i, 0d);
            } else {
                double rate = (double)stageStatus[i] / len; // 실패율 계산
                len -= stageStatus[i]; // 다음 스테이지 도전자 수 = 전 스테이지 도전자 수 - 클리어 못 한 사람의 수
                fRate.put(i, rate);
            }
        }

        List<Integer> list = new ArrayList<>(fRate.keySet());

        list.sort(new Comparator<Integer>() { // key 값으로 내림차순 정렬
            @Override
            public int compare(Integer o1, Integer o2) {
                return Double.compare(fRate.get(o2), fRate.get(o1));
            }
        });

        for(int i = 0; i < N; i++) { // answer에 정렬된 값으로 stage 출력
            answer[i] = list.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        FailureRate f = new FailureRate();
        int[] x = {2,1,2,6,2,4,3,3};
        f.solution(5,x);
    }
}

// 코드 참고: https://soobinhand.tistory.com/50

// 문제를 읽다가 HashMap으로 풀면 좋겠다는 생각이 들었으나 정작 어떻게 구현해야할지 감이 잡히지 않아서 오랫동안 어버버거렸다
// 내가 잘 하고 잇는걸까...