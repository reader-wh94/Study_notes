package Retry;

// https://programmers.co.kr/learn/courses/30/lessons/86491

public class Rectangle {
    public int solution(int[][] sizes) {
        int[] width = new int[sizes.length];
        int[] height = new int[sizes.length];
        int maxW = 0;
        int maxH = 0;

        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][0] < sizes[i][1]) {
                width[i] = sizes[i][0];
                height[i] = sizes[i][1];
            } else {
                width[i] = sizes[i][1];
                height[i] = sizes[i][0];
            }
        }

        for(int num : width) {
            if(maxW < num)
                maxW = num;
        }

        for(int num : height) {
            if(maxH < num)
                maxH = num;
        }
        
        return maxW * maxH;
    }
}
