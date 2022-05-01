#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

double xold, x, b, r;
int p;
bool flag;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (cin >> xold) {
        if (!xold) {
            return 0;
        }
        flag = true;
        x = fabs(xold);
        for (b = 2; b*b <= x; b++) {
            r = b*b;
            for (p = 2; r < x; p++) {
                r *= b;
            }
            if (r == x) {
                if (xold > 0 || p % 2) {
                    cout << p << endl;
                    flag = false;
                    break;
                }
            }
        }
    if (flag) {
        cout << 1 << endl;
    }
    }
}