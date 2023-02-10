package 프로그래머스.레벨0.Day20;

public class 유한소수_판별하기 {
    class Solution {
        public int solution(int a, int b) {
            int newB = b / GCD(a, b);

            while (newB != 1) {
                if (newB % 2 == 0) {
                    newB /= 2;
                } else if (newB % 5 == 0) {
                    newB /= 5;
                } else {
                    return 2;
                }
            }

            return 1;
        }
        private int GCD (int a, int b) {
            if (b == 0) {
                return a;
            } else {
                return GCD (b, a % b);
            }
        }
    }
}
