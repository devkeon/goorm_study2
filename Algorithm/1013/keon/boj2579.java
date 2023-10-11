import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static Integer[] dp;
    static int[] stair;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dp = new Integer[300];
        stair = new int[300];

        for(int i = 0; i < n; i++){
            stair[i] = Integer.parseInt(br.readLine());
        }
        dp[0] = stair[0];
        dp[1] = dp[0] + stair[1];
        dp[2] = Math.max(dp[0] + stair[2], stair[1] + stair[2]);

        for(int i = 3; i < n; i++){
            dp[i] = Math.max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]);
        }
        System.out.println(dp[n - 1]);
    }
}
