#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int step[301];
int n;
int dp[301]={0,};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    for(int i=1;i<=n;i++){
        cin >> step[i];
    }
    dp[1]=step[1];
    dp[2]=step[1]+step[2];
    dp[3]=max(step[1]+step[3],step[1]+step[2]);

    for(int i=4;i<=n;i++){
        dp[i]=max(dp[i-2]+step[i],dp[i-3]+step[i-1]+step[i]);
    }

    cout << dp[n] << endl;

}