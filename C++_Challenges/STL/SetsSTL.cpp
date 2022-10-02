#include <iostream>
#include <set>
using namespace std;


int main() {
    set<int>s;
    int Q, i, y, x;
    bool is_in;

    cin>>Q;
    for (int i = 0; i < Q; i++) {
        cin>>y>>x;
        if (y == 1)
            s.insert(x);

        else if (y==2)
            s.erase(x);
        
        else
            if (s.find(x) != s.end())
                cout<<"Yes"<<endl;
            else
                cout<<"No"<<endl;
    }
    return 0;
}



