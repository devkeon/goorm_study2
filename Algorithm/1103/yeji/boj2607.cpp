#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
  int N;
  int answer = 0;
  string str;
  int str_size;

  cin >> N;
  cin >> str;
  str_size = str.length(); // 기준 문자열 길이

  map<char,int> dict;
  for(auto it : str){
    dict[it]++;
  }

  for(int i=0;i<N-1;i++){
    string text;
    int text_size;
    cin >> text;
    text_size = text.length(); // 비교 문자열 길이

    map<char,int> copy_dict;
    map<char,int>::iterator iter;
    copy_dict = dict;//?


    int same = 0;
    for(int t=0;t<text_size;t++){
      if(copy_dict.find(text[t])!=copy_dict.end()){
        if(copy_dict[text[t]]>0){
          copy_dict[text[t]]--;
          same++;
        }
      }
    }
    if(str_size == text_size){
      if(str_size == same || str_size == same + 1){
        answer++;
      }
    }
    else if(str_size - 1 == text_size && same == str_size - 1){
      answer++;
    }else if(str_size + 1 == text_size && same == str_size){
      answer++;
    }else continue;
  }
  cout << answer << endl;

}