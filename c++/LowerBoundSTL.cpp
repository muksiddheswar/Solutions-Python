#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

    int n, k, q, p, idx;
    vector<int> v;
    vector<int> arr;
    vector <int> :: iterator lower;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> k;
        v.push_back(k);
    }

    cin >> q;

    for(int i = 0; i < q; i++)
    {
        cin >> k;
        arr.push_back(k);
    }

    sort(v.begin(), v.end());
    for(int i = 0; i < q; i++)
    {
        lower = lower_bound(v.begin(), v.end(), arr[i]); 
        idx = (lower - v.begin());

        if(v.at(idx) == arr[i])
        {
            cout << "Yes " << idx+1  << endl;
        }
        else
        {
            cout << "No " << idx+1 << endl;  
        }
    }   

    return 0;
}
