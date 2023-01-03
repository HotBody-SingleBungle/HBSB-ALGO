package 프로그래머스.레벨0.Day4;

public class 피자_나눠_먹기_1 {
    class Solution {
        public int solution(int n) {
            int pizza = 1;
            while ((pizza * 7) - n < 0) {
                pizza++;
            }
            return pizza;
        }
    }
}
