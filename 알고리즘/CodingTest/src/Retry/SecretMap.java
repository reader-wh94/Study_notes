package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/17681

public class SecretMap {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for(int i = 0; i < n; i++) {
            answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]);
        }

        for(int i = 0; i < n; i++) {
           answer[i] =  String.format("%"+n+"s", answer[i]); // key point -> n만큼의 문자열을 담을 수 있도록 해야한다!
           answer[i] = answer[i].replace("1", "#");
           answer[i] = answer[i].replace("0", " ");
        }
        return answer;
    }
}
