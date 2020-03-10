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

    int num1; int num2; int num3;
    cin >> num1;
    cin >> num2;
    num3 = num2*2 - num1;
    cout << num3;

}
