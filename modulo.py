nums = []
for n in range(10):
    nums.append(input())
nums = [int(n) for n in nums]
mods = [n % 42 for n in nums]
mods = set(mods)
print(len(mods))