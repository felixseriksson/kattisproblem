#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

vector<int> cover(pair<double, double> G, vector<pair<double, double>> I) {
    vector<int> S(I.size());
    vector<int> R;
    for (int i = 0; i < S.size(); i++) {
        S[i] = i;
    }
    sort(S.begin(), S.end(), [&](int a, int b) { return I[a] < I[b]; });
    double curr = G.first;
    int idx = 0;
    while (curr < G.second || R.empty()) {
        pair<double, int> mx = make_pair(curr, -1);
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
    double a, b;
    int n;
    while(cin >> a >> b) {
        cin >> n;
        vector<pair<double,double>> vec;
        double c, d;
        for (int i = 0; i < n; i++) {
            cin >> c >> d;
            vec.push_back(make_pair(c, d));
        }
        vector<int> ans = cover(make_pair(a, b), vec);
        if (ans.empty()) {
            cout << "impossible" << endl;
        }
        else {
            sort(ans.begin(), ans.end());
            cout << ans.size() << endl;
            for (int i = 0; i < ans.size(); i++) {
                cout << ans.at(i) << " ";
            }
            cout << endl;
        }
    }
}