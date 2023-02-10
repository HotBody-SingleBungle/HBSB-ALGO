package 프로그래머스.레벨0.Day23;

public class 치킨_쿠폰 {
    class Solution {
        public int solution(int chicken) {
            int answer = 0;
            while (chicken >= 10) {
                answer += chicken / 10;
                chicken = chicken / 10 + chicken % 10;
            }
            return answer;
        }
    }
}
