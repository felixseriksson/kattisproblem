#include <bits/stdc++.h>
//#include <cmath>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cout << setprecision(20);

    long double rad; long double area; long double taxicabarea; long double pi = 3.14159265358979323846264338327950288419716939937510;
    cin >> rad;
    area = pi * rad * rad;
    taxicabarea = 2 * rad * rad;
    cout << area << endl;
    cout << taxicabarea << endl;

}
