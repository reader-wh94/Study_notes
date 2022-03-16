package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/68935

public class Ternary {
    public int solution(int n) {
        int answer = 0;
        String a = "";
        StringBuffer sb = new StringBuffer();

        while(n != 0) {
            a = (n % 3) + a;
            n /= 3;
        }

        a = sb.append(a).reverse().toString();
        answer = Integer.parseInt(a, 3);
        return answer;
    }
}
