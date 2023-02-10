package 프로그래머스.레벨0.Day24;
import java.util.*;
public class 특이한_정렬 {
    class Solution {
        public int[] solution(int[] numlist, int n) {

            for (int i = 0; i < numlist.length - 1; i++) {
                for (int j = i + 1; j < numlist.length; j++) {
                    if (Math.abs(numlist[i] - n) > Math.abs(numlist[j] - n) || (Math.abs(numlist[i] - n) == Math.abs(numlist[j] - n) && numlist[i] < numlist[j])) {
                        int temp = numlist[i];
                        numlist[i] = numlist[j];
                        numlist[j] = temp;

                    }
                }
            }
            return numlist;
        }
    }
}
