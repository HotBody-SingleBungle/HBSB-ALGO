package 프로그래머스.레벨0.Day19;

public class 다항식_더하기 {
    class Solution {
        public String solution(String polynomial) {
            String answer = "";
            String sArr[] = polynomial.split(" ");
            int strNum = 0;
            int num = 0;

            for (int i = 0; i < sArr.length; i++) {
                if (sArr[i].contains("x") && sArr[i].length() > 1) {
                    strNum += Integer.parseInt(sArr[i].substring(0, sArr[i].length() -1));
                } else if (sArr[i].contains("x") && sArr[i].length() == 1) {
                    strNum += 1;
                } else if (!sArr[i].contains("x") && !sArr[i].contains("+")) {
                    num += Integer.parseInt(sArr[i]);
                }
            }

            if (strNum > 0 && num > 0) {
                if (strNum == 1) {
                    answer = "x" + " + " + String.valueOf(num);
                } else {
                    answer = String.valueOf(strNum) + "x" + " + " + String.valueOf(num);
                }

            } else if (strNum > 0) {
                if (strNum == 1) {
                    answer = "x";
                } else {
                    answer = String.valueOf(strNum) + "x";
                }

            } else if (num > 0) {
                answer = String.valueOf(num);
            }

            return answer;
        }
    }
}
