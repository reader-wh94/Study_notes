package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/12977

public class MakePrime {
    public int solution(int[] nums) {
        int answer = 0;

        for(int i = 0; i < nums.length; i++) {
            for(int j = i+1; j < nums.length; j++) {
                for(int k = j+1; k < nums.length; k++) {
                    if(isPrime(nums[i] + nums[j] + nums[k])){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }

    private boolean isPrime(int num) {
        for(int i = 2; i < num; i++) {
            if(num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        MakePrime m = new MakePrime();
        int[] arr = {1,2,3,4};
        m.solution(arr);
    }
}
