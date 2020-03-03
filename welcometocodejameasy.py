def issubsequence(string1, string2, len1, len2):
    #tests if string1 is a subsequence of string2
    #obs: måste göras om från att testa om till att räkna antal
    if len1 == 0:
        return True
    if len2 == 0:
        return False

    if string1[len1-1] == string2[len2-1]:
        return issubsequence(string1, string2, len1-1, len2-1)

    return issubsequence(string1, string2, len1, len2-1)

cases = 3

for n in range(cases):
    inputtemp = input()
    if issubsequence("welcome to code jam", inputtemp, len("welcome to code jam"), len(inputtemp)):
        print("yes")
    else:
        print("no")