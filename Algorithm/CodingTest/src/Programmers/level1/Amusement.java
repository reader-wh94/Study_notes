package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/82612

public class Amusement {
    public long solution(int price, int money, int count) {
        long answer = -1;
        boolean prices = true;
        boolean counts = true;
        long sum = 0;

        if(price <= 0 && price > 2500) prices = false;
        if(count <= 0 && count > 2500) counts = false;

        if(prices && counts) {
            for(int i = 1; i <= count; i++) {
                sum += (price * i);
            }

            if(money < sum) answer = sum - money;
            else answer = 0;
        }

        return answer;
    }
}
