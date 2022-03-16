package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/86051

public class NoExist {
    public int solution(int[] numbers) {
        int answer = -1;
        int sum = 45;

        for(int i : numbers) {
            sum -= i;
        }
        answer = sum;

        return answer;
    }
}
// 처음에 반복문으로 numbers에 있는 숫자를 확인 -> 제거 한 후 [0~9]까지 남아있는 숫자들을 더해서 return 하는 방법을 생각
// 0~9까지의 총 합 45에서 numbers에 있는 숫자들을(서로 같은 숫자가 없기 때문에 이 방법이 가능) 빼고 남은 수를 return 하는 방법이 있었다.
// 뭔가 더 쉬운 방법이 있겠지 했는데 생각이 안나서 검색해봤더니 저런 방법이 있었다. 어디를 놓친걸까 생각해보니 역시나 같은 숫자가 없다는 포인트를 놓쳤다.
