import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj2579 {

  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    int[] dp = new int[n+1];
    int[] stair = new int[n+1];

    for (int i = 1; i <= n; i++) {
      stair[i] = Integer.parseInt(br.readLine());
    }

    dp[1] = stair[1];

    if (n >= 2) {
      dp[2] = stair[2] + stair[1];
    }

    for(int i = 3; i <= n; i++) {
      dp[i] = Math.max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2]);
    }

    System.out.println(dp[n]);
  }
}