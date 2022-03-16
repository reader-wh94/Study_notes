package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12943

public class Collatz {
    public int solution(long num) {
        // num에 int 값을 넘어가는 숫자가 연산 중에 입력되기 때문에 int -> long으로 타입 변환해야한다.
        // 626331 이라는 3번째 tc에 3을 곱하면서 연산이 계속 되기 때문에 int형 말고 long형을 써야한다.
        int answer = 0;

        while(num != 1) {
            answer++;
            if(num % 2 == 0) {
                num /= 2;
            } else {
                num = num * 3 + 1;
            }

            if(answer == 500) {
                answer = -1;
                break;
            }
        }
        return answer;
    }
}
