import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] dp = new int[100001];
        int[] sq = new int [321];
        Arrays.fill(dp, 100001);
        for(int i = 1; i <= 320; i++){
            if(i*i <= 100001){
                dp[i*i] = 1;
            }
            sq[i] = i*i;
        }

        for(int i = 1; i <= N; i++){
            if(dp[i] == 1){
                continue;
            }
            for(int j = 1; j <= sq.length; j++){
                if(sq[j] > i){
                    break;
                }

                int tmp = Math.min(dp[i-1] + 1, dp[i-sq[j]] + 1);
                dp[i] = Math.min(tmp, dp[i]);
            }
        }

        System.out.println(dp[N]);

    }
}