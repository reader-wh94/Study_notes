package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/81301

public class EngNum {
    public int solution(String s) {
        int answer = 0;
        String[] eng = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

        for(int i = 0; i < 10; i++) { // 0~9까지 숫자가 있기 때문
            s = s.replace(eng[i], num[i]);
        }

        answer = Integer.parseInt(s);
        return answer;
    }
    // if 문이나 switch 문을 사용해서 replace를 사용하는 방법이 아니라 0~9까지를 배열에 담아놓고(이미 값이 다 고정되어 있기 때문)
    // 그 배열에서 replace를 하는 방법이 더 깔끔하고 빠르게 된다.
}
