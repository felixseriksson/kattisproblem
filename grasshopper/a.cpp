#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int offsets[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

int bfs(int r, int c, int gr, int gc, int lr, int lc) {
    int grid[r][c];
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            grid[i][j] = 10000;
        }
    }
    grid[gr-1][gc-1] = 0;
    queue<pair<int, int>> q;
    q.push(make_pair(gr-1, gc-1));
    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();
        
        if ((curr.first == lr-1) && (curr.second == lc-1)) {
            return grid[lr-1][lc-1]; 
        }

        for (int i = 0; i < 8; i++) {
            int newr = curr.first + offsets[i][0];
            int newc = curr.second + offsets[i][1];
            if ((newr >= 0) && (newr < r) && (newc >= 0) && (newc < c)) {
                if (grid[curr.first][curr.second] + 1 < grid[newr][newc]) {
                    grid[newr][newc] = grid[curr.first][curr.second] + 1;
                    q.push(make_pair(newr, newc));
                }
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int r, c, gr, gc, lr, lc, ans;
    while(cin >> r >> c >> gr >> gc >> lr >> lc) {
        ans = bfs(r, c, gr, gc, lr, lc);
        if (ans == -1) {
            cout << "impossible" << endl;
        } else {
            cout << ans << endl;
        }
    }
}