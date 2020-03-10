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

    ll rad; ll crust; double a1; double atot;
    cin >> rad; cin >> crust;
    a1 = (rad-crust) * (rad-crust);
    atot = rad * rad;
    cout << a1/atot * 100;
    
}
