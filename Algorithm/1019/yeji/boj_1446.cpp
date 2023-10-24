#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, d;
vector<pair<int,int> > shortcut[10001];

void input(){
    for(int i=0;i<n;i++){
        int from,to,way;
        cin >> from >> to >> way;
        //⭐️도착지점인덱스 값에 {출발지점, 지름길거리} 를담아주는것
        shortcut[to].emplace_back(from,way);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> d;
    
    // dp배열
    vector<int> dp(d+1,1e9);
    
    //지름길 갯수 만큼 입력을 받는다.
    input();
    
    
    // 0 번째의 비용은 0으로
    dp[0]=0;
    
    
    //목적지 d까지 지름길로 가는 경우와 걸어가는 경우를 비교해주면서 최소값을 계산
    for(int i=1;i<=d;i++){
        if(shortcut[i].size()==0){
            dp[i]=dp[i-1]+1; // 직전 누적값 + 1 🚶‍♀️걸었으니까
        }else{
            for(auto it : shortcut[i]){
                dp[i] = min(dp[i],min(dp[i-1]+1,dp[it.first]+it.second));
            }
        }
    }
    cout << dp[d] << '\n';
    
    
}