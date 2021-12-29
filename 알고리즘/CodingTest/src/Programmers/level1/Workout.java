package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/42862

public class Workout {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] students = new int[n];

        for(int i: lost) students[i-1]--; // 체육복 잃어버린 학생
        for(int i: reserve) students[i-1]++; // 여분의 체육복이 있는 학생

        for(int i = 0; i < students.length; i++) {
            if(students[i] == -1) { // 체육복이 없는 경우
                if(i > 0 && students[i-1] == 1) { // 앞에서 빌려줌
                    students[i]++;
                    students[i-1]--;
                } else if(i < n-1 && students[i+1] == 1) { // 뒤에서 빌려줌
                    students[i]++;
                    students[i+1]--;
                } else { // 체육복을 빌리지 못한 경우
                    answer--;
                }
            }
        }
        return answer;
    }
}

// 코드 참고: https://jionchu.tistory.com/9