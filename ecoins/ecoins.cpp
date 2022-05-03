#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <queue>
#include <math.h>
using namespace std;

double emodulus(pair<int, int> a) {
    return sqrt(a.first*a.first + a.second*a.second);
}

int bfs(vector<pair<int, int>> v, int s) {
    int grid[s+1][s+1];
    for (int i = 0; i <= s; i++) {
        for (int j = 0; j <= s; j++) {
            grid[i][j] = 1000;
        }
    }
    grid[0][0] = 0;
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    pair<int, int> curr;
    pair<int, int> next;
    while (!q.empty()) {
        curr = q.front();
        q.pop();
        for (auto coin : v) {
            next.first = curr.first + coin.first;
            next.second = curr.second + coin.second;
            if (emodulus(next) > s) {
                continue;
            }
            else if (emodulus(next) == s) {
                return grid[curr.first][curr.second] + 1;
            }
            else {
                if (grid[curr.first][curr.second] + 1 < grid[next.first][next.second]) {
                    grid[next.first][next.second] = grid[curr.first][curr.second] + 1;
                    q.push(make_pair(next.first, next.second));
                }
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    while (N--) {
        int n, s;
        cin >> n >> s;
        vector<pair<int, int>> v;
        int a, b;
        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            v.push_back(make_pair(a, b));
        }

        int ans = bfs(v, s);

        if (ans == -1) {
            cout << "not possible" << endl;
        }
        else {
            cout << ans << endl;
        }

        if (N != 0) {
            cin;
        }
    }
    return 0;
}