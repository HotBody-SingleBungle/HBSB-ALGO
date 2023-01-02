package 프로그래머스.레벨0.Day2;

public class 배열_두배_만들기 {
    class Solution {
        public int[] solution(int[] numbers) {
            for (int i = 0; i < numbers.length; i++){
                numbers[i] *= 2;
            }
            return numbers;
        }
    }
}
