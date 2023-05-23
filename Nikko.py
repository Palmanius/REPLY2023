def June(a):
    day = 1 
    week = []

    for i in range(a-1):
        week.append(" ")

    month = [["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]]

    while day<31:
        if len(week)<7:
            week.append(""+str(day)+" ")
            day+=1
        else:
            month.append(week)
            week = []
    month.append(week)
    return month
    
FirstJune = 3
print(June(FirstJune))


import random
array = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,0]
count = 0
random.shuffle(array)
for i in array[1:]:
    if i>array[array.index(i)-1]:
        count += 1
        print(array,count)