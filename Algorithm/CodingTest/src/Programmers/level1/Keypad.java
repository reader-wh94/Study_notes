package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/67256

public class Keypad {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int leftIndex = 10;
        int rightIndex = 12;

        for(int i : numbers) {
            if(i == 1 || i == 4 || i == 7) {
                answer += "L";
                leftIndex = i;
            } else if (i == 3 || i == 6 || i == 9) {
                answer += "R";
                rightIndex = i;
            } else {
                if(i == 0) {
                    i += 11; // 0을 눌렀을 경우에는 11로 변경
                }
                int ld = ((Math.abs(i - leftIndex)) / 3) + ((Math.abs(i - leftIndex)) % 3);
                int rd = ((Math.abs(i - rightIndex)) / 3) + ((Math.abs(i - rightIndex)) % 3);
                if(ld == rd) {
                    if(hand.equals("right")) {
                        answer += "R";
                        rightIndex = i;
                    } else {
                        answer += "L";
                        leftIndex = i;
                    }
                } else if(ld > rd) {
                    answer += "R";
                    rightIndex = i;
                } else if(ld < rd) {
                    answer += "L";
                    leftIndex = i;
                }
            }
        }

        return answer;
    }
}

// 코드 참고 : https://dud0880.tistory.com/11