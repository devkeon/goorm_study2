import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj1446 {
  
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int D = Integer.parseInt(st.nextToken());

    int[] dp = new int[D+1]; //해당 위치까지 가장 짧은 거리를 저장할 배열
    int[][] shortCut = new int[N][3]; //지름길 정보를 저장할 배열

    for (int i = 0; i < N; i++) {
        st = new StringTokenizer(br.readLine());
        shortCut[i][0] = Integer.parseInt(st.nextToken());
        shortCut[i][1] = Integer.parseInt(st.nextToken());
        shortCut[i][2] = Integer.parseInt(st.nextToken());
    } //지름길 정보 저장

    /**
     * 가장 짧은 거리로 도달하는 방법
     * 1. 지름길이 있는 경우 지름길을 이용 (가장 짧은 거리를 보장하진 않음)
     * 2. 직전까지 오는 가장 짧은 거리 + 1
     **/
    Arrays.fill(dp, Integer.MAX_VALUE);
    dp[0] = 0;

    for (int i = 1; i < dp.length; i++) {
      for (int j = 0; j < shortCut.length; j++) {
        if (i == shortCut[j][1]) {
          dp[i] = Math.min(dp[i], Math.min(dp[i-1]+1, dp[shortCut[j][0]] + shortCut[j][2]));
        } else {
          dp[i] = Math.min(dp[i], dp[i-1]+1);
        }
      }
    }

    System.out.println(dp[D]);
  }
}