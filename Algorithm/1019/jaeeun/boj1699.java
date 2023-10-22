import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1699 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(bf.readLine());
    
    int[] dp = new int[N+1]; 
    
    dp[0] = 0;

    //최소 개수가 되는 경우: N에 가장 가까운 제곱수를 뺀 dp값 + 1
    for (int i = 1; i <= N; i++) {
      dp[i] = i; //1의 제곱으로만 표현한 개수로 초기화
      for (int j = 1; j * j <= i; j++) {
        dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
      }
    }
    System.out.println(dp[N]);
  }
}