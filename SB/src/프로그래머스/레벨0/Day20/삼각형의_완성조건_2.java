package 프로그래머스.레벨0.Day20;

public class 삼각형의_완성조건_2 {
    /*
    bigValue + smallValue > x
    smallValue + x > bigValue
    x > bigValue - smallValue
    bigValue + smallValue > x > bigValue - smallValue
    x = bigValue + smallValue - bigValue - smallValue - 1
*/

    class Solution {
        public int solution(int[] sides) {
            int bigValue = Math.max(sides[0], sides[1]);
            int smallValue = Math.min(sides[0], sides[1]);

            int lowLimit = bigValue - smallValue;
            int highLimit = bigValue + smallValue;

            return highLimit - lowLimit - 1;
        }
    }
}
