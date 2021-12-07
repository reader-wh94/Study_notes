package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/42748

import java.util.ArrayList;
import java.util.Collections;

public class K {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i = 0; i < commands.length; i++) {
            ArrayList<Integer> arr = new ArrayList<Integer>();
            for(int j = commands[i][0]-1; j < commands[i][1]; j++) {
                arr.add(array[j]);
            }
            Collections.sort(arr);
            answer[i] = arr.get(commands[i][2] - 1);
        }

        return answer;
    }
}

// copyOfRange를 사용하는 방법도 있다
// 2차 배열이라고 아방하게 있지 말자
