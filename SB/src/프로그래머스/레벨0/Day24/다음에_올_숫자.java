package 프로그래머스.레벨0.Day24;

public class 다음에_올_숫자 {
    class Solution {
        public int solution(int[] common) {
            int answer = 0;

            if (common[1] - common[0] == common[2] - common[1]) {
                answer = common[common.length-1] + common[2] - common[1];
            } else {
                answer = common[common.length-1] * (common[1] / common[0]);
            }

            return answer;
        }
    }
}
