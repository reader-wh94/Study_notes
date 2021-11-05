package Programmers.level1;

import java.util.*;


public class AddArray {
    public List<Integer> solution(int[] numbers) {
        ArrayList<Integer> arr = new ArrayList<Integer>();

        for(int i = 0; i < numbers.length; i++) {
            for(int j = 0; j < numbers.length; j++) {
                if(i != j) {
                    arr.add(numbers[i] + numbers[j]);
                }
            }
        }

        TreeSet<Integer> data = new TreeSet<Integer>(arr); // TreeSet으로 중복 제거
        List<Integer> answer = new ArrayList<Integer>(data);

        return answer;
    }
}
