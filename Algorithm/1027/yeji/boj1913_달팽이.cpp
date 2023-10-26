#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

long long int Map[1001][1001];
long long int N;
long long int m;
long long int square;



void print(){
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            cout << Map[i][j] << " ";
        }
        cout << '\n';
    }
}

pair<int,int> find(int target){
    pair<int,int> answer;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            if(Map[i][j]==target){
                answer.first = i;
                answer.second = j;
            }
        }
    }
    return answer;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // 좌표크기
    cin >> N;
    // 찾는 값
    cin >> m;


    square = pow(N,2);
    
    int Cycle = N/2+1;

    int x = 1;
    int y = 0;

    int n = N;
    while(Cycle--){

        // down
        for(int i=0;i<n;i++){
            y+=1;
            Map[y][x]=square--;
        }

        // right
        for(int i=0;i<n-1;i++){
            x+=1;
            Map[y][x]=square--;
        }

        // up
        for(int i=0;i<n-1;i++){
            y-=1;
            Map[y][x]=square--;
        }

        // left
        for(int i=0;i<n-2;i++){
            x-=1;
            Map[y][x]=square--;
        }
        n-=2;
    }


    
    
    print();

    pair<int,int> res;
    
    res = find(m);

    cout << res.first << " " <<res.second << endl;


    
    
    

    
}