inp = [ord(x) for x in input()]
for i in range(len(inp)-2):
    if inp[i] == 58 and inp[i+1] == 41:
        print(i)
    elif inp[i] == 59 and inp[i+1] == 41:
        print(i)
    elif inp[i] == 58 and inp[i+1] == 45 and inp[i+2] == 41:
        print(i)
    elif inp[i] == 59 and inp[i+1] == 45 and inp[i+2] == 41:
        print(i)
if inp[-2] == 58 and inp[-1] == 41:
    print(len(inp)-2)
elif inp[-2] == 59 and inp[-1] == 41:
    print(len(inp)-2)