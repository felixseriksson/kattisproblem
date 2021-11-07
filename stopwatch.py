t = int(input())
s = 0
for i in range(t):
    s += ((-1)**(i+1))*int(input())
if t % 2:
    print("still running")
else:
    print(s)