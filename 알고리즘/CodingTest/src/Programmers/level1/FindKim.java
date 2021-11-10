package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12919

public class FindKim {
    public String solution(String[] seoul) {
        String answer = "";

        for(int i = 0; i < seoul.length; i++) {
            // if (seoul[i] == "Kim") { String의 비교는 == 이 아니라 .equals를 사용해야 한다
            if(seoul[i].equals("Kim")) {
                String a = Integer.toString(i);
                answer = "김서방은 " + a + "에 있다";
            }
        }
        return answer;
    }
}
