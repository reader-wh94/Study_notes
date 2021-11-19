package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12921

public class Prime {
    /* public int solution(int n) { // 시간 초과로 실패
        int answer = 0;

        for(int i = 2; i <= n; i++){
            for(int j = 2; j <= i; j++) {
                if(i % j == 0) {
                    if(i == j) answer++;
                    else  break;
                }
            }
        }
        return answer;
    } */
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n+1];

        for(int i = 2; i <= n; i++) {
            arr[i] = i; // arr에 소수인 2부터 n까지 저장 (2~n까지의 수를 소수인지 비교하기 위함)
        }

        for(int i = 2; i < n; i++) {
            for(int j = 2 * i; j <= n; j += i) { // 2를 제외한 짝수는 소수가 아님 (j는 4부터 시작됨) + 자신의 배수는 소수가 아님
                arr[j] = 0;
            }
        }

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != 0) answer++; // 0이 아닌 것들의 개수를 리턴(소수의 개수)
        }
        return answer;
    }
}
