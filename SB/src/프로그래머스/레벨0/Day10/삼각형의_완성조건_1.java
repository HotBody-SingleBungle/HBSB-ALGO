package 프로그래머스.레벨0.Day10;

import java.util.*;

public class 삼각형의_완성조건_1 {
    class Solution {
        public int solution(int[] sides) {
            int answer = 0;
            Arrays.sort(sides);

            if (sides[2] < sides[0] + sides[1])
                answer = 1;
            else
                answer = 2;

            return answer;
        }
    }
}
