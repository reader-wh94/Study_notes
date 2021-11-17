package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12901

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;

public class Day {
    public String solution(int a, int b) {
        String answer = "";

        LocalDate date = LocalDate.of(2016, a, b); // LocalDate 생성
        DayOfWeek dayOfWeek = date.getDayOfWeek(); // DayofWeek 객체를 구하고
        answer = dayOfWeek.getDisplayName(TextStyle.SHORT, Locale.US); // 해당 날짜의 요일을 구함, 요일이 "Tue"로 출력된다
        answer = answer.toUpperCase(); // "TUE"로 변경하기 위해 대문자로 변경

        return answer;
    }
}
