package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/77484

public class Lotto {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int min = 0;
        int max = 0;

        for(int i = 0; i < 6; i++) {
            if(lottos[i] == 0) max++;
            for(int j = 0; j < 6; j++) {
                if(win_nums[j] == lottos[i]) min++;
            }
        }

        answer[1] = grade(min);
        answer[0] = grade(min + max);

        return answer;
    }

    public int grade(int m) {
        int grade = 0;

        switch (m) {
            case 6:
                grade = 1;
                break;
            case 5:
                grade = 2;
                break;
            case 4:
                grade = 3;
                break;
            case 3:
                grade = 4;
                break;
            case 2:
                grade = 5;
                break;
            default:
                grade = 6;
                break;
        }
        return grade;
    }
}
