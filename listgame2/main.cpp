#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

vi reduct(vi v, const vi &p) {
  for (int i = 0; i < p.size(); ++i)
    if (!v[p[i]]--) return vi();
  return v;
}

int gen(vector<int> v, vector<int> lb, int tobeat) {
  int tot = 0;
  for (int i = 0; i < v.size(); ++i) tot += v[i];

  if (lb.empty()) lb.push_back(0);
  else
  for (int i = 0; ++lb[i] >= v.size(); ++i) {
    if (i == lb.size()-1) {
      lb = vi(lb.size()+1, 0);
      break;
    } else {
      lb[i] = lb[i+1]+1;
      for (int j = 0; j < i; ++j)
	lb[j] = lb[i];
    }
  }

  if (tobeat >= tot/lb.size()) return tobeat;
  vi g = reduct(v, lb);
  if (!g.empty()) tobeat = 1+gen(g, lb, max(tobeat-1, 0));
  tobeat = gen(v, lb, tobeat);
  return tobeat;
}

int main(void) {
  ll X;
  vector<int> v;
  scanf("%lld", &X);
  int k = 0;
  for (ll p = 2; p*p <= X; ++p) {
    int e = 0;
    while (X % p == 0) X /= p, ++e;
    if (e) {
      ++k;
      if (e > 1) v.push_back(e-1);
    }
  }
  if (X != 1) ++k;
  vi lb(1, v.size());
  if (!v.empty()) k += gen(v, lb, 0);
  printf("%d\n", k, "end?");
  int q;
  cin >> q;
  return 0;
}

