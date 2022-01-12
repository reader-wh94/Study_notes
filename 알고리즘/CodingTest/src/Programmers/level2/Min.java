package Programmers.level2;

// https://programmers.co.kr/learn/courses/30/lessons/12941

import java.util.Arrays;
import java.util.Collections;

public class Min {
    public int solution(int []A, int []B) {
        int answer = 0;
        Integer[] b = new Integer[B.length];

        for(int i = 0; i < B.length; i++) {
            b[i] = B[i];
        }

        Arrays.sort(A);
        Arrays.sort(b, Collections.reverseOrder());

        // Integer[] b = Arrays.stream(B).boxed().toArray(Integer[]::new);
        // 효율성 테스트에서 실패가 뜬다. stream이 생각보다 시간을 많이 쓰는 것 같다

        for(int i = 0; i < A.length; i++) {
            answer += A[i] * b[i];
        }
        return answer;
    }
}
