package 프로그래머스.레벨0.Day8;

import java.util.*;

public class 최댓값_만들기_1 {
    class Solution {
        public int solution(int[] numbers) {
            int answer = 0;
            Arrays.sort(numbers);

            return numbers[numbers.length - 1] * numbers[numbers.length - 2];
        }
    }
}
