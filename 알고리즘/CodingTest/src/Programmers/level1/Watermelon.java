package Programmers.level1;

public class Watermelon {
    public String solution(int n) {
        String answer = "";
        String[] a = {"수", "박"};
        String[] b = new String[n];

        for(int i = 0; i < n; i++) {
            if(i % 2 == 0) b[i] = "수";
            else b[i] = "박";
        }

        answer = String.join("", b);

        return answer;
    }
}
