package 프로그래머스.레벨0.Day15;

public class 컨트롤_제트 {
    class Solution {
        public int solution(String s) {
            int answer = 0;
            String split[] = s.split(" "); // 공백을 기준으로 잘라서 배열에 저장

            for (int i = 0; i < split.length; i++) {
                if (split[i].equals("Z")) { // 값이 Z인 경우
                    answer -= Integer.parseInt(split[i - 1]); // 이전 index값을 빼줌
                } else {
                    answer += Integer.parseInt(split[i]); // 현재 index값을 더해줌
                }

            }
            return answer;
        }
    }
}
