def zeller(year, month, day):
    if month == 1 or month == 2:
        month += 12
        year -= 1

    c = year // 100
    y = year % 100
    m = month
    d = day
    W = c // 4 - 2 * c + y + y // 4 + 26 * (m + 1) // 10 + d - 1
    if W < 0:
        return (W + (-W // 7 + 1) * 7) % 7
    return W % 7

count=0

for year in range(1900,2001):
    for month in range(1,13):
        if zeller(year,month,1)==0:
            count+=1
            
print(count)