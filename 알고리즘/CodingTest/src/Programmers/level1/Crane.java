package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/64061

import java.util.Stack;

public class Crane {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> bucket = new Stack<Integer>(); // 바구니

        for(int i = 0; i < moves.length; i++) {
            for(int j = 0; j < board.length; j++) {
                if(board[j][moves[i] - 1] != 0) { // 위,아래로 인형을 탐색하기 때문에 행이 바뀌어야 함 ex) (0,0), (1,0)
                    if(bucket.isEmpty()) { // bucket이 비어있는 경우 > 해당 인형 넣기
                        bucket.push(board[j][moves[i] - 1]);
                    } else {
                        if(bucket.peek() == board[j][moves[i] - 1]) { // bucket이 비어있지 않은 경우 > 맨 위의 인형과 새로 넣은 인형이 같은 지 비교
                            bucket.pop();
                            answer += 2;
                        } else { // bucket의 top과 board에서 선택한 인형이 다를 경우 bucket에 저장
                            bucket.push(board[j][moves[i] - 1]);
                        }
                    }
                    board[j][moves[i] - 1] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}

// 코드 참고: https://zzang9ha.tistory.com/224