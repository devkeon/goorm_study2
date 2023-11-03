#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
  string str;
  cin >> str;

  int a= 0;
  int answer = str.length();
  // 문자열 길이로 초기화
  
  for(auto c: str){
    if(c == 'a'){
      a++;
    }
  }

  for(int i=0;i<str.length();i++){
    int cnt = a, temp = 0;
    for(int j=i;j<i+str.length();j++){
      if(cnt == 0){
        break;
      }
      if(str[j%str.size()]== 'b'){ // b이면
        temp++; // 교환 횟수 ++
        cnt--; // 교환해줄 a 수 감소
      }
      else{
        cnt--; // b가 아니더라도, 교환해줄 a 수 감소
      }
    }
    answer = min(answer, temp);
  }

  cout << answer << '\n';
}