package 프로그래머스.레벨0.Day13;

public class 제곱수_판별하기 {
    class Solution {
        public int solution(int n) {

            if (n % Math.sqrt(n) == 0)
                return 1;
            else
                return 2;
            // for (int i = 1; i <= n; i++) {
            //     if ((double)n / i - i == 0)
            //         return 1;
            // }
            // return 2;
        }
    }
}
