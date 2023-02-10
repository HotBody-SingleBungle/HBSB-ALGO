package 프로그래머스.레벨0.Day19;

public class 캐릭터의_좌표 {
    class Solution {
        public int[] solution(String[] keyinput, int[] board) {
            int[] answer = {0, 0};

            for (int i = 0; i < keyinput.length; i++) {
                if (keyinput[i].equals("up") && answer[1] < board[1] / 2) {
                    answer[1] += 1;
                } else if (keyinput[i].equals("down") && answer[1] > - board[1] / 2) {
                    answer[1] -= 1;
                } else if (keyinput[i].equals("left") && answer[0] > - board[0] / 2) {
                    answer[0] -= 1;
                } else if (keyinput[i].equals("right") && answer[0] < board[0] / 2) {
                    answer[0] += 1;
                }
            }
            return answer;
        }
    }
}
