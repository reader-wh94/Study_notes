package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/17681

public class SecretMap {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for(int i = 0; i < n; i++) {
            answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]); // 2진법으로 변경, 비트 연산으로 배열 2개를 한 번에 1,0으로 구분
        }

        for(int i = 0; i < n; i++) {
            answer[i] = String.format("%"+n+"s", answer[i]); // n개의 자릿수만큼 문자열 담기
            answer[i] = answer[i].replace("1", "#");
            answer[i] = answer[i].replace("0", " ");
        }
        return answer;
    }
}
// 2진법으로 만들면서 바로 비트 연산을 하는 아이디어는 생각하지 못했다...
// replace 말고 1이상일 경우 배열을 #으로 바꾸는 생각을 했었는데 replace가 더 간단하고 알아보기 쉬운 것 같다.
