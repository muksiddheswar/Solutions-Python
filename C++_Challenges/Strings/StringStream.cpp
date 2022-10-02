#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    stringstream s(str);
    vector<int> g1;
    char ch;
    int t;
    while (s >> t){
        g1.push_back(t);
        s >> ch;
    }

    return g1;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}