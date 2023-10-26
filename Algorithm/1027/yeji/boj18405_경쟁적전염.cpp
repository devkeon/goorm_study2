#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N,K;
int S,X,Y;
int MAP[201][201];
//queue<pair<int,int> > q[1004];

int dy[4]={0,0,-1,1};
int dx[4]={-1,1,0,0};
bool visited[201][201]={false,};




priority_queue<pair<int,pair<int,int> > , vector<pair<int,pair<int,int> > >, greater<pair<int,pair<int,int> > > > q;
vector<pair<int,int> > virus[1004];



// 초기화
void init(){
    for(int i=0;i<201;i++){
        for(int j=0;j<201;j++){
            visited[i][j]=false;
        }
    }

    for(int i=0;i<1004;i++){
        virus[i].clear();
    }

}

void print(){
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            cout << MAP[i][j] << " ";
        }
        cout << '\n';
    }
}


void input(){
    
    // 크기, K이하 자연수
    cin >> N >> K;
    
    // MAP 입력받기
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            cin >> MAP[i][j];
            if(MAP[i][j]!=0){
                q.push(make_pair(MAP[i][j],make_pair(i,j)));
            }
        }
    }
    
    // 시간, 좌표
    cin >> S >> Y >> X;
}


void infection(){
    while(!q.empty()){
        int value = q.top().first;
        int cy = q.top().second.first;
        int cx = q.top().second.second;

        q.pop();

        for(int i=0;i<4;i++){
            int ny = cy+dy[i];
            int nx = cx+dx[i];

            if(ny>=0 && nx>=0 && ny<=N && nx<=N){
                if(!visited[ny][nx] && MAP[ny][nx]==0){
                    MAP[ny][nx] = value;
                    visited[ny][nx]=true;
                    virus[value].emplace_back(ny,nx);
                }
            }
        }

    }


    // 0인 구간에서 전염된 애들 값을 다시 q 에 넣기
    for(int i=1;i<=K;i++){
        for(int j=0;j<virus[i].size();j++){
            int y = virus[i][j].first;
            int x = virus[i][j].second;

            q.push(make_pair(MAP[y][x],make_pair(y,x)));
        }
    }
}




int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    input();

    if(S==0){
        cout << MAP[Y][X] << endl;
        return 0;
    }


    while(S--){
        infection();
        init();

        
    }

    //print();

    if(MAP[Y][X]){
        cout << MAP[Y][X] << endl;
    }else{
        cout << 0 << endl;
    }







}