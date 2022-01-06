package Retry;

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
