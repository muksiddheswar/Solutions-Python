#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int N,i, temp, temp1;
    vector<int> v;
    cin>>N;

    for(i=0;i<N;i++){
        cin>>temp;
        v.push_back(temp);
    }

    cin>>temp;
    v.erase(v.begin()+temp-1);

    cin>>temp>>temp1;
    v.erase(v.begin()+temp-1,v.begin()+temp1-1);

    cout<<v.size()<<endl;
    for(i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }

    return 0;
}
