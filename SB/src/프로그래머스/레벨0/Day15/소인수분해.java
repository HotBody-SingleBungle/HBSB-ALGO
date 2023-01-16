package 프로그래머스.레벨0.Day15;
import java.util.*;
public class 소인수분해 {
    class Solution {
        public ArrayList solution(int n) {
            ArrayList<Integer> list = new ArrayList<>();

            for (int i = 2; i <= n; i++) {
                while (n % i == 0) {
                    if (!list.contains(i)) {
                        list.add(i);
                    }
                    n /= i;
                }
            }

            return list;
        }
    }
}
