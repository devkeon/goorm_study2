import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1063 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    String[] moveTypes = {"R", "L", "B", "T", "RT", "LT", "RB", "LB"};
    int[] dx = {0, 0, -1, 1, 1, 1, -1, -1};
    int[] dy = {1, -1, 0, 0, 1, -1, 1, -1};

    char[] king = st.nextToken().toCharArray();
    char[] pawn = st.nextToken().toCharArray();
    int N = Integer.parseInt(st.nextToken());

    //킹의 위치
    int kingX = Character.getNumericValue(king[1]); 
    char kingY = king[0];
    
    //폰의 위치
    int pawnX = Character.getNumericValue(pawn[1]); 
    char pawnY = pawn[0];

    //킹 이동
    for (int i = 0; i < N; i++) {
      String move = br.readLine();

      int kingNx = 0, pawnNx = 0;
      char kingNy = 0, pawnNy = 0;

      for (int j = 0; j < moveTypes.length; j++) {
        if (moveTypes[j].equals(move)) {
          kingNx = kingX + dx[j];
          kingNy = (char)(kingY + dy[j]);
          pawnNx = pawnX;
          pawnNy = pawnY;

          if (kingNx == pawnX && kingNy == pawnY) {
            pawnNx = pawnX + dx[j];
            pawnNy = (char)(pawnY + dy[j]);
          }
        }
      }

      if (kingNx >= 1 && kingNy >= 'A' && kingNx <= 8 && kingNy <= 'H' && pawnNx >= 1 && pawnNy >= 'A' && pawnNx <= 8 && pawnNy <= 'H') {
        kingX = kingNx;
        kingY = kingNy;
        pawnX = pawnNx;
        pawnY = pawnNy;
      } else continue;
    }

    System.out.println(kingY + "" + kingX);
    System.out.println(pawnY + "" + pawnX);
  }
}