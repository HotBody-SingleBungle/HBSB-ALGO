package 프로그래머스.레벨0.Day5;

public class 양꼬치 {
    class Solution {
        public int solution(int n, int k) {
            int sheep = n * 12000;
            int drink = k * 2000;
            int service = n / 10;
            int answer = sheep + drink - service * 2000;

            return answer;
        }
    }
}
