#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cout << setprecision(10);

    int n, m;
    cin >> n >> m;
    while( n != 0 && m != 0) {
        set<int> sett;
        for(int i = 0; i < n+m; i++) {
            int val;
            cin >> val;
            sett.insert(val);
        }
        int doubles = n + m - sett.size();
        //cout << sett.size() << endl;
        cout << doubles << endl;
        cin >> n >> m;
    }
    //int end;
    //cin >> end;


}
