#include <iostream>
#include <map>
using namespace std;

int main() {
    map<int,int>s;
    
    int Q, i, y, x, z;
    bool is_in;

    cin>>Q;
    for (int i = 0; i < Q; i++) {
        cin>>y;
        if (y == 1){
            cin>>x>>z;

            auto search = s.find(x);

            if (search != s.end())
                search->second += z;
            else
                s.insert(make_pair(x,z));

            }

        else if (y==2){
            cin>>x;
            s.erase(x);
        }
        
        else
            cin>>x;
            auto search = s.find(x);
            if (search != s.end())
                cout<<0<<endl;
            else
                cout<<search->second<<endl;
    }
    return 0;
}



