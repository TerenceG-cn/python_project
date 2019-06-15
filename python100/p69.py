numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
j = 1
count = numList.__len__()

while count > 3:
    for i in numList:
        if numList[i] != 0:
            if j % 3 == 0:
                numList[i] = 0
                j = 1
                count -= 1
            else:
                j += 1
        print(numList)
