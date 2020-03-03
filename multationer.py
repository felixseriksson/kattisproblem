startingpoint = [x for x in input()]
goal = [x for x in input()]

tempfilters = []
numberoftimes = []
scores = []
for n in range(len(goal)-2):
    combo = "".join(goal[n:n+3])
    if combo not in tempfilters:
        tempfilters.append(combo)
        numberoftimes.append(1)
    else:
        numberoftimes[tempfilters.index(combo)] += 1
for n in range(len(goal)-1):
    combo = "".join(goal[n:n+2])
    if combo not in tempfilters:
        tempfilters.append(combo)
        numberoftimes.append(1)
    else:
        numberoftimes[tempfilters.index(combo)] += 1
for n in range(len(goal)):
    combo = goal[n]
    if combo not in tempfilters:
        tempfilters.append(combo)
        numberoftimes.append(1)
    else:
        numberoftimes[tempfilters.index(combo)] += 1
for combo in range(len(tempfilters)):
    scores.append((len(tempfilters[combo])-1) * numberoftimes[combo])

print(tempfilters)
print(numberoftimes)
print(scores)

#IDÉ: Gå bakifrån, kolla vilka "maps" som ens är möjliga (Ex. BBCB så skulle ju inte CB kunna ha
# kommit från B) sen köra för bara dem och repetera