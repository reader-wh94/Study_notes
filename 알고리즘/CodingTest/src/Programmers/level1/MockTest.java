package Programmers.level1;

import java.util.ArrayList;

public class MockTest {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] p1 = {1,2,3,4,5};
        int[] p2 = {2,1,2,3,2,4,2,5};
        int[] p3 = {3,3,1,1,2,2,4,4,5,5};
        int[] score = new int[3];

        // p1~p3에 answers.length 만큼 답을 넣고 시작하는 것이 아니라 (시간이 더 오래 걸렸을 듯)
        // 특정 패턴 만큼 답을 넣어놓고 p1[(i % answers.length)] 이런 식으로 답을 맞춰봐야한다

/*        for(int i = 0; i < answers.length; i++) {
            if(p1[i % answers.length] == answers[i]) score[0] += 1;
            if(p2[i % answers.length] == answers[i]) score[1] += 1;
            if(p3[i % answers.length] == answers[i]) score[2] += 1;
        }
 */
        // answers.length를 사용하면 런타임 에러가 발생한다. p1, p2, p3의 크기는 고정적이니 숫자로 변환해서 사용하니까 통과
        for(int i = 0; i < answers.length; i++) {
            if(p1[i % 5] == answers[i]) {score[0]++;}
            if(p2[i % 8] == answers[i]) {score[1]++;}
            if(p3[i % 10] == answers[i]) {score[2]++;}
        }

        int max = Math.max(score[0], Math.max(score[1], score[2]));

        ArrayList<Integer> arr = new ArrayList<Integer>();
        if(max == score[0]) arr.add(1);
        if(max == score[1]) arr.add(2);
        if(max == score[2]) arr.add(3);

        answer = new int[arr.size()];

        for(int i = 0; i < answer.length; i++) {
            answer[i] = arr.get(i);
        }

        return answer;
    }
}
