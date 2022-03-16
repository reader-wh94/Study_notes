package Programmers.level1;
import java.lang.Math;

// https://programmers.co.kr/learn/courses/30/lessons/12934

public class Sqrt {
    public long solution(long n) {
        long res = (long)(Math.sqrt(n));

        if(n == Math.pow(res, 2)) { // key: 제곱근과 제곱된 값을 비교
            return (long)Math.pow(res + 1 , 2);
        } else {
            return -1;
        }
    }
}
