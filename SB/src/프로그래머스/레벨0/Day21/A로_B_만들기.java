package 프로그래머스.레벨0.Day21;
import java.util.*;
public class A로_B_만들기 {
    class Solution {
        public int solution(String before, String after) {
            char beforeCharArr[] = before.toCharArray();
            char afterCharArr[] = after.toCharArray();
            Arrays.sort(beforeCharArr);
            Arrays.sort(afterCharArr);
            before = String.valueOf(beforeCharArr);
            after = new String(afterCharArr);
            if (before.equals(after)) {
                return 1;
            } else {
                return 0;
            }

        }
    }
}
