package Programmers.level1;
// https://programmers.co.kr/learn/courses/30/lessons/12950

public class MatrixAddition {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];
        // column의 개수는 arr1[0].length로 설정
        for(int i = 0; i < arr1.length; i++) {
            for(int j = 0; j < arr1[0].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }

}
