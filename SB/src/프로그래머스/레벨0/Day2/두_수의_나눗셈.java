package 프로그래머스.레벨0.Day2;

public class 두_수의_나눗셈 {
    class Solution {
        public int solution(int num1, int num2) {
            double answer = (double)num1 / num2 * 1000;
            return (int)answer;
        }
    }
}
