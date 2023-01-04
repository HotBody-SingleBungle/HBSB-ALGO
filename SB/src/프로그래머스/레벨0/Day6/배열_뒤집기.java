package 프로그래머스.레벨0.Day6;

public class 배열_뒤집기 {
    class Solution {
        public int[] solution(int[] num_list) {
            int[] answer = new int[num_list.length];
            for (int i = 0; i < num_list.length; i++) {
                answer[i] = num_list[num_list.length - i -1];
            }
            return answer;
        }
    }
}
