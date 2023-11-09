import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj14719 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int H = Integer.parseInt(st.nextToken());
    int W = Integer.parseInt(st.nextToken());

    int[] height = new int[W];
    int result = 0;

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < W; i++) {
      height[i] = Integer.parseInt(st.nextToken());
    }

    for (int i = 1; i < W - 1; i++) {
      int left = 0;
      int right = 0;

      for (int j = 0; j < i; j++) {
        left = Math.max(left, height[j]);
      }

      for (int j = i + 1; j < W; j++) {
        right = Math.max(right, height[j]);
      }

      if (height[i] < left && height[i] < right) {
        result += Math.min(left, right) - height[i];
      }
    }

    System.out.println(result);
  }
}