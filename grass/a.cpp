#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <queue>
#include <math.h>
using namespace std;

vector<int> cover(pair<long double, long double> G, vector<pair<long double, long double>> I) {
    vector<int> S(I.size());
    vector<int> R;
    for (int i = 0; i < S.size(); i++) {
        S[i] = i;
    }
    sort(S.begin(), S.end(), [&](int a, int b) { return I[a] < I[b]; });
    long double curr = G.first;
    int idx = 0;
    while (curr < G.second || R.empty()) {
        pair<long double, int> mx = make_pair(curr, -1);
        while (idx < I.size() && I[S[idx]].first <= curr) {
            mx = max(mx, make_pair(I[S[idx]].second, S[idx]));
            idx++;
        }
        if (mx.second == -1) {
            return {};
        }
        curr = mx.first;
        R.push_back(mx.second);
    }
    return R;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long double l, w;
    while(cin >> n >> l >> w) {
        vector<pair<long double,long double>> vec;
        long double a, b;
        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            vec.push_back(make_pair(a, b));
        }

        vector<pair<long double, long double>> actualvec;
        pair<long double, long double> curr;
        long double ca, cb;
        long double lr;
        for (int i = 0; i < n; i++) {
            curr = vec.at(i);
            ca = curr.first;
            cb = curr.second;
            if (2*cb < w) {
                continue;
            }
            lr = sqrt(cb*cb - w*w/4);
            actualvec.push_back(make_pair(ca - lr, ca + lr));
        }

        vector<int> ans = cover(make_pair(0, l), actualvec);
        if (ans.empty()) {
            cout << -1 << endl;
        }
        else {
            cout << ans.size() << endl;
        }
    }
}