package 동계_대학생_SW_알고리즘_특강_사전문제;

import java.util.Scanner;

public class 현석이의_생일 {
    static int N;
    static int card;
    static int max;
    static int numbers[];
    static int input[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            max = 0;
            N = sc.nextInt();
            int x = sc.nextInt();
            int y = sc.nextInt();

            if (N < y) {
                if (N < x || x == 0) {
                    System.out.println("#" + test_case + " " + -1);
                    continue;
                }
            }

            card = 1; // 배열의 크기를 결정 할 변수
            int temp = N;
            while (temp > 10) {
                if (temp % 10 > 0) {
                    card++;
                    temp /= 10;
                }
            }

            numbers = new int[card];
            input = new int[2];
            input[0] = x;
            input[1] = y;

            permutation(0);
            System.out.println("#" + test_case + " " + max);
        }


    }

    private static void permutation(int cnt) {
        if (card == cnt) {
            int possible = 0;
            int a = 1;
            for (int i = cnt - 1; i >= 0 ; i--) {
                possible += numbers[i] * a;
                a *=10;
            }

            if (N > possible && max < possible)
                max = possible;
            return;
        }

        for (int i = 0; i < 2; i++) {
            numbers[cnt] = input[i];
            permutation(cnt + 1);
        }

    }
}
