# class SegmentTree(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.max_value = {}
#         self.sum_value = {}
#         self.len_value = {}
#         self._init(start, end)

#     def out_of_bounds_check(self, start, end):
#         start = max(start, self.start)
#         end = min(end, self.end)
#         if start > end:
#             return None, None
#         return start, end

#     def add(self, start, end, weight=1):
#         start, end = self.out_of_bounds_check(start, end)
#         if start is None:
#             return False
#         self._add(start, end, weight, self.start, self.end)
#         return True

#     def query_max(self, start, end):
#         start, end = self.out_of_bounds_check(start, end)
#         if start is None:
#             return None
#         return self._query_max(start, end, self.start, self.end)

#     def query_sum(self, start, end):
#         start, end = self.out_of_bounds_check(start, end)
#         if start is None:
#             return 0
#         return self._query_sum(start, end, self.start, self.end)

#     def query_len(self, start, end):
#         start, end = self.out_of_bounds_check(start, end)
#         if start is None:
#             return 0
#         return self._query_len(start, end, self.start, self.end)

#     """"""
#     def _init(self, start, end):
#         self.max_value[(start, end)] = 0
#         self.sum_value[(start, end)] = 0
#         self.len_value[(start, end)] = 0
#         if start < end:
#             mid = start + int((end - start) / 2)
#             self._init(start, mid)
#             self._init(mid+1, end)

#     def _add(self, start, end, weight, in_start, in_end):
#         key = (in_start, in_end)
#         if in_start == in_end:
#             self.max_value[key] += weight
#             self.sum_value[key] += weight
#             self.len_value[key] = 1 if self.sum_value[key] > 0 else 0
#             return

#         mid = in_start + int((in_end - in_start) / 2)
#         if mid >= end:
#             self._add(start, end, weight, in_start, mid)
#         elif mid+1 <= start:
#             self._add(start, end, weight, mid+1, in_end)
#         else:
#             self._add(start, mid, weight, in_start, mid)
#             self._add(mid+1, end, weight, mid+1, in_end)
#         self.max_value[key] = max(self.max_value[(in_start, mid)], self.max_value[(mid+1, in_end)])
#         self.sum_value[key] = self.sum_value[(in_start, mid)] + self.sum_value[(mid+1, in_end)]
#         self.len_value[key] = self.len_value[(in_start, mid)] + self.len_value[(mid+1, in_end)]

#     def _query_max(self, start, end, in_start, in_end):
#         if start == in_start and end == in_end:
#             ans = self.max_value[(start, end)]
#         else:
#             mid = in_start + int((in_end - in_start) / 2)
#             if mid >= end:
#                 ans = self._query_max(start, end, in_start, mid)
#             elif mid+1 <= start:
#                 ans = self._query_max(start, end, mid+1, in_end)
#             else:
#                 ans = max(self._query_max(start, mid, in_start, mid),
#                         self._query_max(mid+1, end, mid+1, in_end))
#         #print start, end, in_start, in_end, ans
#         return ans

#     def _query_sum(self, start, end, in_start, in_end):
#         if start == in_start and end == in_end:
#             ans = self.sum_value[(start, end)]
#         else:
#             mid = in_start + int((in_end - in_start) / 2)
#             if mid >= end:
#                 ans = self._query_sum(start, end, in_start, mid)
#             elif mid+1 <= start:
#                 ans = self._query_sum(start, end, mid+1, in_end)
#             else:
#                 ans = self._query_sum(start, mid, in_start, mid) + self._query_sum(mid+1, end, mid+1, in_end)
#         return ans

#     def _query_len(self, start, end, in_start, in_end):
#         if start == in_start and end == in_end:
#             ans = self.len_value[(start, end)]
#         else:
#             mid = in_start + int((in_end - in_start) / 2)
#             if mid >= end:
#                 ans = self._query_len(start, end, in_start, mid)
#             elif mid+1 <= start:
#                 ans = self._query_len(start, end, mid+1, in_end)
#             else:
#                 ans = self._query_len(start, mid, in_start, mid) + self._query_len(mid+1, end, mid+1, in_end)

#         #print start, end, in_start, in_end, ans
#         return ans

# n = int(input())
# segtree = SegmentTree(1, n)
# nums = [int(input()) for _ in range(n)]
# print(nums)
# nums = sorted(enumerate(nums, start=1), key=lambda x: x[1])
# print(nums)
# segtree.add(1, n+1, 1)

# for i,j in zip(range(1, n//2+1), range(n, n//2, -1)):
#     iindex = nums[i-1][0] # vill sortera nummer i på pos iindex
#     # print(i)
#     # print(iindex)
#     print(segtree.query_sum(1, iindex))
#     segtree.add(i,i,-1)
#     jindex = nums[j-1][0]
#     # print(j)
#     # print(jindex)
#     print(segtree.query_sum(jindex,n+1))
#     segtree.add(j,j,-1)

# if n % 2:
#     # index = nums[n//2][0]
#     # print(n//2+1)
#     # print(index)
#     print(0)
n = int(input())
nums = [int(input()) for _ in range(n)]
# print(nums)
nums = sorted(enumerate(nums, start=1), key=lambda x: x[1])
# print(nums)


N = 100000;

tree = [0] * (2 * N);

# function to build the tree
def build(arr) :

	# insert leaf nodes in tree
	for i in range(n) :
		tree[n + i] = arr[i];
	
	# build the tree by calculating parents
	for i in range(n - 1, 0, -1) :
		tree[i] = tree[i << 1] + tree[i << 1 | 1];

# function to update a tree node
def updateTreeNode(p, value) :
	
	# set value at position p
	tree[p + n] = value;
	p = p + n;
	
	# move upward and update parents
	i = p;
	
	while i > 1 :
		
		tree[i >> 1] = tree[i] + tree[i ^ 1];
		i >>= 1;

# function to get sum on interval [l, r)
def query(l, r) :

	res = 0;
	
	# loop to find the sum in the range
	l += n;
	r += n;
	
	while l < r :
	
		if (l & 1) :
			res += tree[l];
			l += 1
	
		if (r & 1) :
			r -= 1;
			res += tree[r];
			
		l >>= 1;
		r >>= 1
	
	return res;

build([1]*n)
for i,j in zip(range(1, n//2+1), range(n, n//2, -1)):
    iindex = nums[i-1][0] # vill sortera nummer i på pos iindex
    # print(i)
    # print(iindex)
    print(query(0, iindex-1))
    updateTreeNode(iindex-1, 0)
    jindex = nums[j-1][0]
    # print(j)
    # print(jindex)
    print(query(jindex,n))
    updateTreeNode(jindex-1, 0)

if n % 2:
    # index = nums[n//2][0]
    # print(n//2+1)
    # print(index)
    print(0)