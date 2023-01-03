package 프로그래머스.레벨0.Day4;

public class 배열의_평균값 {
    class Solution {
        public double solution(int[] numbers) {
            double sum = 0;
            for (int i = 0; i < numbers.length; i++) {
                sum += numbers[i];
            }

            return sum / numbers.length;
        }
    }
}
