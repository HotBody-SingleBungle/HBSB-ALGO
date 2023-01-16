package 프로그래머스.레벨0.Day16;
import java.util.*;
public class 최댓값_만들기_2 {
    class Solution {
        public int solution(int[] numbers) {
            Arrays.sort(numbers);

            return Math.max(numbers[numbers.length - 1] * numbers[numbers.length - 2], numbers[0] * numbers[1]);
        }
    }
}
