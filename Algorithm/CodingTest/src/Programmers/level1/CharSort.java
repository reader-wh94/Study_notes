package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12915

import java.util.*;

public class CharSort {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];

        ArrayList<String> arr = new ArrayList<String>();

        for(int i = 0; i < strings.length; i++) {
            arr.add(strings[i].charAt(n) + strings[i]); // 정렬의 기준이 되는 문자+전체 단어
        }

        Collections.sort(arr); // 정렬

        for(int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i).substring(1); // 맨 앞의 문자 삭제 후 전체 단어를 answer에 저장
        }
        return answer;
    }
}

// Comparator를 사용하여 정렬를 해볼까 했는데 해당 라이브러리를 사용하는 것보다 ArrayList를 사용하는 방법이 더 익숙해 보였다.
// 14번째 코드처럼 정렬의 기준이 되는 문자에 해당 단어 전체를 붙여 정렬한 후 앞에 글자만 따로 떼서 저장한다는 아이디어는 생각하지 못 했었는데
// 고민하다가 다른 사람들의 코드를 참고했더니 이런 방법으로 푼 사람들도 있어서 정말 아이디어의 차이에 대해서 뭔가 반성해야겠다는 생각이 들었다.