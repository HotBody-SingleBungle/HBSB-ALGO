package 프로그래머스.레벨0.Day11;

public class 모스부호_1 {
    class Solution {
        public String solution(String letter) {
            String answer = "";
            String[] morse = {".-", "-...", "-.-.", "-..", ".", "..-.",
                    "--.", "....", "..", ".---", "-.-", ".-..",
                    "--", "-.", "---", ".--.", "--.-", ".-.",
                    "...", "-", "..-", "...-", ".--", "-..-",
                    "-.--", "--.."};

            String arr[] = letter.split(" ");

            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < morse.length; j++) {
                    if (arr[i].equals(morse[j])) {
                        answer += (char)(j + 97);
                    }
                }
            }
            return answer;
        }
    }
}
