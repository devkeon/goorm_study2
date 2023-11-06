import java.util.Scanner;

public class boj1522 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();

    int min = Integer.MAX_VALUE;
    int aCount = 0;

    for (int i = 0; i < str.length(); i++) {
      if (str.charAt(i) == 'a') {
        aCount++;
      }
    }

    for(int i=0; i<str.length(); i++) {
			int bCount = 0;
			for(int j = i; j < i + aCount; j++) {
				int idx = j % str.length();
				if(str.charAt(idx) == 'b') {
					bCount++;
				}
			}
			min = Math.min(min, bCount);
		}
		
		System.out.println(min);
    sc.close();
  }
}
