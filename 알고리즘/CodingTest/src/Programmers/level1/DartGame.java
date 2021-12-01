package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/17682

public class DartGame {
    public int solution(String dartResult) {
        int answer = 0;
        int[] round = new int[3]; // 3 라운드의 게임 점수를 저장할 배열
        char[] options = dartResult.toCharArray();
        int idx = -1;

        for(int i = 0; i < dartResult.length(); i++) {
            if(options[i] >= '0' && options[i] <= '9') {
                idx++;
                round[idx] += Integer.parseInt(String.valueOf(options[i]));
                if(i+1 != options.length-1 && options[i+1] == '0' && options[i] == '1') { // 10점을 얻었을 경우
                    round[idx] -= Integer.parseInt(String.valueOf(options[i])); // round에 들어간 값(1)을 제거
                    round[idx] = 10; // 1이 아닌 10을 저장
                    i++; // 다음 options 검사
                }
            } else if(options[i] == 'D') { // S는 1제곱이라 상관 없음
                round[idx] *= round[idx];
            } else if(options[i] == 'T') {
                round[idx] *= round[idx] * round[idx];
            } else if(options[i] == '*') {
                if(idx > 0) {
                    round[idx-1] *= 2;
                }
                round[idx] *= 2;
            } else if(options[i] == '#') {
                round[idx] *= -1;
            }
        }

        answer = round[0] + round[1] + round[2];
        return answer;
    }
}
// 알바 갔다와서 다시 풀어 봅시다