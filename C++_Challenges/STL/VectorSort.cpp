#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,i, temp;;
    vector<int> v;
    cin>>N;

    for(i=0;i<N;i++){
        cin>>temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());

    for(i=0;i<N;i++){
        cout<<v[i]<<" ";
    }
    return 0;
}
