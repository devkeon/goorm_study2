#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int dp[100001];

    int n;
    cin >> n;


    for(int i=1;i<=n;i++){
        dp[i] = i; // 1의 제곱수로하면 그냥 해당 숫자씩 저장됨 ex) dp[7] = 7
        for(int j=1;j*j<=i;j++){
            dp[i] = min(dp[i],dp[i-j*j]+1);
        }
    }

    cout << dp[n] << '\n';

    

}