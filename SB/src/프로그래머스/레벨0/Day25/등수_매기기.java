package 프로그래머스.레벨0.Day25;

import java.util.*;

public class 등수_매기기 {

    class Solution {
        public int[] solution(int[][] score) {
            List<Integer> scoreList = new LinkedList<>();

            for (int[] s : score) {
                scoreList.add((s[0] + s[1]));
            }
            scoreList.sort(Comparator.reverseOrder());

            int[] answer = new int[score.length];
            for (int i = 0; i < score.length; i++) {
                answer[i] = scoreList.indexOf(score[i][0] + score[i][1]) + 1;
            }
            return answer;
        }
    }
}
