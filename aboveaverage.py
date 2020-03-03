'''
cases = int(input())
for n in range(cases):
    above = 0
    grades = list(str(input()).split())
    number = int(grades.pop(0))
    for n in range(number):
        grades[n] = int(grades[n])
    
    average = float((float(sum(grades)))/number)
    if int(average) == 0:
        print("0.000%")
        continue
    for grade in grades:
        if float(grade) > average:
            above += 1

    percentage = round(float(above/number)*100, 3)
    percentage = "{:.3f}".format(percentage)
    string = str(percentage)
    string = string + "%"
    print(string)
    #print(strpercentage)
    #print(strpercentage + "00%")
    
    if len(strpercentage) == 4:
        strpercentage = strpercentage + "00"
        print(strpercentage + "%")
    elif len(strpercentage) == 5:
        strpercentage = strpercentage + "0"
        print(strpercentage + "%")
    elif len(strpercentage) == 6:
        print(strpercentage + "%")
'''
def getaverage(values):
    return float(sum(values)/len(values))

cases =  int(input())
for case in range(cases):
    grades = list(input().split())
    grades = list(map(float,grades))
    numberofstudents = int(grades.pop(0))
    average = getaverage(grades)
    counter = 0
    for grade in grades:
        if grade > average:
            counter += 1
        else:
            pass
    above = counter
    percentage = float((above/numberofstudents)*100)
    percentagefixed = str("%.3f"%percentage)
    print(percentagefixed + "%")