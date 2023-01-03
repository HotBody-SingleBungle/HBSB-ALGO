package 프로그래머스.레벨0.Day3;

import java.util.*;

public class 최빈값_구하기 {
    class Solution {
        public int solution(int[] array) {
            Arrays.sort(array);

            int modArr[] = new int [array[array.length - 1] + 1];

            for (int i : array) {
                modArr[i]++;
            }

            int mode = 0;
            int numCount = 0;

            for (int i = 0; i < modArr.length; i++) {
                if (modArr[i] > numCount) {
                    numCount = modArr[i];
                    mode = i;
                }
            }
            int sameNumCount = 0;
            for (int i = 0; i < modArr.length; i++) {
                if (modArr[i] == numCount) {
                    sameNumCount++;
                    if (sameNumCount > 1) {
                        mode = -1;
                        break;
                    }

                }
            }

            return mode;
        }
    }
}
