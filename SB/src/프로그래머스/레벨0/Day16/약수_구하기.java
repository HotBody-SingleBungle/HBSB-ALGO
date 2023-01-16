package 프로그래머스.레벨0.Day16;
import java.util.*;
public class 약수_구하기 {
    class Solution {
        public ArrayList solution(int n) {
            ArrayList<Integer> list = new ArrayList<>();

            for (int i = 1; i <= n; i++) {
                if (n % i == 0) {
                    list.add(i);
                }
            }

            return list;
        }
    }
}
