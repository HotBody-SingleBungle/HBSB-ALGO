package 프로그래머스.레벨0.Day6;

public class 배열_원소의_길이 {
    class Solution {
        public int[] solution(String[] strlist) {
            int[] answer = new int[strlist.length];

            for (int i = 0; i < strlist.length; i++) {
                answer[i] = strlist[i].length();

            }
            return answer;
        }
    }
}
