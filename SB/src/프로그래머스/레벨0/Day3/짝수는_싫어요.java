package 프로그래머스.레벨0.Day3;

public class 짝수는_싫어요 {
    class Solution {
        public int[] solution(int n) {
            int cnt = 0;
            int arr[] = {};

            if (n % 2 == 0)
                arr = new int[n / 2];
            else
                arr = new int[n / 2 + 1];

            for (int i = 1; i <= n; i++) {
                if (i % 2 == 1) {
                    arr[cnt++] = i;
                }
            }
            return arr;
        }
    }
}
