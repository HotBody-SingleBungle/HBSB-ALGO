package 프로그래머스.레벨0.Day23;

public class 직사각형의_넓이_구하기 {
    class Solution {
        public int solution(int[][] dots) {
            int answer = 0;
            int minX = dots[0][0];
            int minY = dots[0][1];
            int maxX = dots[0][0];
            int maxY = dots[0][1];
            for (int i = 0; i < dots.length; i++) {
                minX = Math.min(minX, dots[i][0]);
                minY = Math.min(minY, dots[i][1]);
                maxX = Math.max(maxX, dots[i][0]);
                maxY = Math.max(maxY, dots[i][1]);
            }
            answer = (maxX - minX) * (maxY - minY);
            return answer;
        }
    }
}
