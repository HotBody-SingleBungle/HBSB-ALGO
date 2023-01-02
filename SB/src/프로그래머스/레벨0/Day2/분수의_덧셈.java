package 프로그래머스.레벨0.Day2;

public class 분수의_덧셈 {
    class Solution {
        public int[] solution(int denum1, int num1, int denum2, int num2) {
            int num = num1 * num2; // 8
            int denum = (denum1 * num2) + (denum2 * num1); // 10
            int GCD = 1;
            for (int i = 1; i <= Math.min(num, denum); i++) {
                if (num % i == 0 && denum % i == 0) {
                    GCD = i;
                }
            }

            int[] answer = {denum / GCD, num / GCD};
            return answer;
        }
    }
}
