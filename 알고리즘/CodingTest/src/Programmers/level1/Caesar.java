package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12926

class Caesar {
    public String solution(String s, int n) { // 띄어쓰기와 z -> a가 아니라 '{'로 넘어가는 예외 처리를 하지 않음
        String answer = "";
        char[] ans = s.toCharArray();
        int[] ans2 = new int[ans.length];
        
        for(int i = 0; i < ans.length; i++) {
            if((int)ans[i])
            ans2[i] = (int)ans[i] + n;
        }
        
        for(int i = 0; i < ans.length; i++) {
            ans[i] = (char)ans2[i];
        }
        
        answer = String.valueOf(ans);
        
        return answer;
    }
  
    public String solution2(String s, int n) {
        String answer = "";
        
        for(int i = 0; i < s.length(); i++) {
        char a = s.charAt(i); // 한 글자씩 n만큼 + 함
        
        if(a >= 'a' && a <= 'z') { // a-z의 범위
          if(a + n > 'z') // a-z의 범위를 벗어나는 경우
            answer += (char)(a + n - 26);
          else answer += (char)(a + n);
        } else if(a >= 'A' && a <= 'Z') { // A-Z의 범위
          if(a + n > 'Z') // A-Z의 범위를 벗어나는 경우
            answer += (char)(a + n - 26);
          else answer += (char)(a+n);
        } else answer += (char)a; // 알파벳이 아닌 다른 경우(띄어쓰기)
      }
       
        return answer;
    }
    
}
