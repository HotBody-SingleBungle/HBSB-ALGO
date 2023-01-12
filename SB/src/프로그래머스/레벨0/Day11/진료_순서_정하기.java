package 프로그래머스.레벨0.Day11;

import java.util.*;

public class 진료_순서_정하기 {
    class Solution {
        public int[] solution(int[] emergency) {
            int[] answer = new int[emergency.length];

            for (int i = 0; i < emergency.length; i++) {
                answer[i]++;
                for (int j = 0; j < emergency.length; j++) {
                    if (emergency[i] < emergency[j]) {
                        answer[i]++;
                    }
                }
            }

            return answer;
        }
    }
}
