package Programmers.level1;
import java.util.*;
// https://programmers.co.kr/learn/courses/30/lessons/12932

public class Reverse {
    public int[] solution(long n) {
        String ans = Long.toString(n);
        char [] arr = ans.toCharArray();
        int [] answer = new int[arr.length];

        for(int i = 0; i < arr.length; i++) {
            answer[i] = Integer.parseInt(arr[arr.length-1-i]+""); // arr[5]여도 배열은 0~4까지 있기 때문에 -1을 함
            // Arrays.sort(answer, Collections.reverseOrder()); -> 역순으로 출력하는게 아니라 내림차순 정렬이 됨
        }

        return answer;
    }
}
