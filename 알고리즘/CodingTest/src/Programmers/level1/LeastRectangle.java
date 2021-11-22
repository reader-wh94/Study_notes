package Programmers.level1;

// https://programmers.co.kr/learn/courses/30/lessons/86491

public class LeastRectangle {
    public int solution(int[][] sizes) {
        int answer = 0;
        int[] width = new int[sizes.length];
        int[] height = new int[sizes.length];
        int maxW = 0;
        int maxH = 0;

        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][0] < sizes[i][1]) {
                height[i] = sizes[i][0];
                width[i] = sizes[i][1];
            }
            else {
                height[i] = sizes[i][1];
                width[i] = sizes[i][0];
            }
        }

        for(int i = 0; i < width.length; i++) {
            if(maxW < width[i]) {
                maxW = width[i];
            }
            if(maxH < height[i]) {
                maxH = height[i];
            }
        }

        answer = maxH * maxW;

        return answer;
    }

    public static void main(String[] args) {
        LeastRectangle l = new LeastRectangle();
        int[][] arr = {{60,50}, {30,70}, {60,30}, {80,40}};

        l.solution(arr);
    }
}
