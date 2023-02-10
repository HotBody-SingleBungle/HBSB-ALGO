package 프로그래머스.레벨0.Day21;

public class OX퀴즈 {
    class Solution {
        public String[] solution(String[] quiz) {
            for (int i = 0; i < quiz.length; i++) {
                String sArr[] = quiz[i].split(" ");
                int result = Integer.parseInt(sArr[0]) + ((sArr[1].equals("+") ? +1 : -1) * Integer.parseInt(sArr[2]));
                quiz[i] = result == Integer.parseInt(sArr[4]) ? "O" : "X";
            }

            return quiz;
        }
    }
}
