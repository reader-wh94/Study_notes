package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/72410

public class NewId {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase(); // 1단계

        String id = ""; // 2단계
        for(int i = 0; i < new_id.length(); i++) {
            char a = new_id.charAt(i);

            if(a >= 'a' && a <= 'z') {
                id += String.valueOf(a);
            } else if(a >= '0' && a <= '9') {
                id += String.valueOf(a);
            } else if(a == '.' || a == '-' || a == '_') {
                id += String.valueOf(a);
            }
        }

        while(id.contains("..")) { // 3단계
            id = id.replace("..", ".");
        }

        if(id.charAt(0) == '.') { // 4단계
            id = id.substring(1, id.length());
        } else if (id.charAt(id.length() - 1) == '.') {
            id = id.substring(0, id.length() - 1);
        }

        if(id.length() == 0) { // 5단계
            id += "a";
        }

        if(id.length() >= 16) { // 6단계
            id = id.substring(0, 15);
        }

        if(id.charAt(id.length() - 1) == '.') {
            id = id.substring(0, id.length() - 1);
        }

        if(id.length() <= 2) { // 7단계
            while(id.length() < 3) {
                id += id.charAt(id.length() - 1);
            }
        }

        return id;
    }

    public static void main(String[] args) {
        NewId i = new NewId();
        i.solution("z-+.^.");
    }
}
