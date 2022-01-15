package Programmers.level2;

// https://programmers.co.kr/learn/courses/30/lessons/12949

public class Matrix {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];

        for(int i = 0; i < arr1.length; i++) {
            for(int j = 0; j < arr2[0].length; j++) {
                for(int k = 0; k < arr1[0].length; k++) {
                    answer[i][j] += (arr1[i][k] * arr2[k][j]);
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Matrix m = new Matrix();
        int[][] arr1 = {{1,4}, {3,2}, {4,1}};
        int[][] arr2 = {{3,3}, {3,3}};
        m.solution(arr1, arr2);
    }
}

// 행렬 정리: https://mathbang.net/562
// 코드 참고: https://velog.io/@delay/programmers12949
/*
    A 열의 개수 == B 행의 개수 -> AxB 가능
    이 때 AB 행렬의 크기는 A 행의 개수 x B 열의 개수
    C[i][j] = A[i][k] + B[k][j]
    K는 A의 열이자 B의 행이다.
 */
